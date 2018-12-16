#
#
#

from p3 import sovleOGA as sovleOGA
from p3 import findOGA as findOGA
from p5 import print2d as print2d
from p5 import print2dx2 as print2dx2
from p5 import sovleOLA as sovleOLA
from p5 import findOLA as findOLA


def main():
    vstr = 'TACGGGTAT'
    ustr = 'GGACGTACG'
    indel = -1
    def scores(x,y):
        ixs = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
        vals = { 0: 'A', 1: 'C', 2: 'G', 3: 'T' }
        matrix = [
            [ 1, -1, -1, -1],
            [-1,  1, -1, -1],
            [-1, -1,  1, -1],
            [-1, -1, -1,  1]
        ]
        return matrix[ixs[x]][ixs[y]]

    # find the score matrix
    table, backtrack = sovleOGA(vstr, ustr, indel, scores)
    print 'table:'
    print2d(table, 3)
    print 'backtrack:'
    print2d(backtrack, 3)
    print 'merged:'
    print2dx2(table, backtrack, 3)

    # find the optimal global alignment
    alignment = findOGA(vstr, ustr, backtrack)
    print 'global alignment'
    print2d(alignment, 0)

    # find the maximal score
    score = table[-1][-1]
    print 'score\n%s' % score

    # find the modified score matrix
    def delta(x, y):
        if x is None or y is None:
            return indel
        return scores(x, y)
    table2, backtrack2 = sovleOLA(vstr, ustr, delta)
    print 'table:'
    print2d(table2, 3)
    print 'backtrack:'
    print2d(backtrack2, 3)
    print 'merged:'
    print2dx2(table2, backtrack2, 3)

    # find the optimal local alignment by score
    score2, loc2, alignment2 = findOLA(vstr, ustr, table2, backtrack2)
    print 'local alignment'
    print2d(alignment2, 0)
    print 'score\n%s' % score2
    print 'location\n%s' % str(loc2)



if __name__ == '__main__':
    main()
