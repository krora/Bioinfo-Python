#!/usr/bin/env python
# Improved breakpoint reversal sort
# Example:  ./prob3.py 8 2 7 6 5 1 4 3
# Based on: cs.helsinki.fi/u/tpkarkka/opetus/14s/AfB/exercise2_problem3.py
import sys
import itertools


# Returns the number of breakpoins.
# Equal to b() in the course book.
# Requires linear time.
def b(u):
    assert u[0] == 0 and u[len(u)-1] == len(u) - 1
    sum = 0
    for i in range(len(u) - 1):
        if u[i] != u[i+1] + 1 and u[i] != u[i+1] - 1:
            #print "Breakpoint:", u[i], u[i+1] 
            sum += 1
    return sum

# Reverses a range of given array in place.
# Simulates the p(i,j) function from course book.
# Requires linear time.
def rev_range(u, i, j):
    assert i <= j and i >= 0 and j >= 0
    assert i < len(u) and j < len(u)
    n = j - i + 1
    for k in range(n/2): 
        # Swap values of k and (n-k-1) in range [i,j]
        u[i+k], u[i+(n-k-1)] = u[i+(n-k-1)], u[i+k]
    return u

# Returns true if given array has a decreasing strip.
# Strips of length one are decreasing by definition (see course book).
# Requires linear time.
def has_decreasing(u):
    assert u[0] == 0 and u[len(u)-1] == len(u) - 1
    for i in range(1, len(u)-1):
        # Element i belongs to a decreasing strip 
        # if the element does not belong to an increasing strip.
        if u[i-1] + 1 != u[i] and u[i] + 1 != u[i+1]:
            return True # u[i] is in decreasing stip
    return False

# Returns the segment whose reversal minimizes 
# the number of breakpoints.
# Brute-force search over all reversals.
# Since b() and rev_range() require linear time,
# this function requires in total O(n^2) time.
def choose_reversal(u):
    assert u[0] == 0 and u[len(u)-1] == len(u) - 1
    max_decr = 0
    max_seg = (0,0)
    br = b(u) # Original number of breakpoints
    for i in range(1, len(u)-2):
        for j in range(i+1, len(u)-1):
            # Evaluate the reversal p(i,j):
            # First check that at least one breakpoint is removed.
            # This check is not necessary but improves time complexity
            # because there are at most 2b reversals that pass the test.
            # This constant time check is performed O(n^2) times.
            if abs(u[i]-u[j+1]) == 1 or abs(u[i-1]-u[j]) == 1:
                # Count how many breakpoints are removed by reversal p(i,j)
                # Passing a shallow copy so that array u does not get modified.
                # This takes O(n) time but is executed at most 2b times.
                a = rev_range(u[:], i, j)
                # if br - b(a) > max_decr:
                if br - b(a) > max_decr or (br - b(a) == max_decr and not has_decreasing(a)):
                    max_decr = br - b(a)
                    max_seg = (i,j)
                    #if max_decr == 2:   # Best we can find
                    #    return (i,j)
    return max_seg

# Returns a segment containing an increasing strip.
# Chooses always the leftmost increasing strip
# (excluding the special elements u[0] and u[len(u)-1]).
# Requires linear time.
def choose_increasing(u):
    assert u[0] == 0 and u[len(u)-1] == len(u) - 1
    i = 1
    while i < len(u)-1 and u[i] + 1 != u[i+1]:
        i += 1
    assert i < len(u)-1
    j = i + 1
    while j < len(u)-2 and u[j] + 1 == u[j+1]:
        j += 1
    return (i, j)

# Implements the improved breakpoint reversal sort.
# The while-loop iterates O(b) times where b is the number of
# breakpoints. The function choose_reversal() requires
# O(n^2) time, thus, the total time complexity
# is O(b \times n^2) where n is the number of elements.
def improvedBreakpointReversalSort(u):
    step = 0
    while b(u) > 0:
        step += 1
        print "step =", step
        u0 = u[:]
        if has_decreasing(u):
            (i, j) = choose_reversal(u)
            rev_range(u, i, j)
        else:
            (i, j) = choose_increasing(u)
            rev_range(u, i, j)
        print u0, "rev_i, rev_j =", i, j
        print u, "b(u) =", b(u)
    return u


def choose_reversal2(u):
    assert u[0] == 0 and u[len(u)-1] == len(u) - 1
    max_decr = 0
    max_seg = (0,0)
    br = b(u) # Original number of breakpoints
    ndall = []
    length = len(u)
    for a in list(itertools.permutations(u[1:-1], length - 2)):
        a = [0] + list(a) + [length - 1]
        if not has_decreasing(a):
            ndall.append(a)
    for u in ndall:
        print "no decr,", u, has_decreasing(u)
    for u in ndall:
        for i in range(1, len(u)-2):
            for j in range(i+1, len(u)-1):
                if abs(u[i]-u[j+1]) == 1 or abs(u[i-1]-u[j]) == 1:
                    a = rev_range(u[:], i, j)
                    if b(u) > b(a):
                        print u, "d(nd) =", b(u)
                        print a, "d(a) =", b(a)
                        print "rev_i, rev_j =", i, j
                        return a

def main2():
    u = [0, 3, 4, 6, 5, 8, 1, 7, 2, 9]
    improvedBreakpointReversalSort(u)

def main4():
    u = [0, 1, 2, 3, 4, 5, 6]
    u = choose_reversal2(u)
    improvedBreakpointReversalSort(u)


print "PROBLEM 2"
main2()
print "PROBLEM 4"
main4()
