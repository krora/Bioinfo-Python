#
#
# en.wikipedia.org/wiki/Needleman-Wunsch_algorithm

from p5 import print2d as print2d
from p5 import print2dx2 as print2dx2


def sovleOGA(vstr, ustr, indel, scores): # general global alignment problem
    nrows = len(vstr) + 1
    ncols = len(ustr) + 1
    table = [[0 for j in range(ncols)] for i in range(nrows)]
    backtrack = [['' for j in range(ncols)] for i in range(nrows)]

    table[0][0] = 0
    for i in range(1, nrows):
        table[i][0] = table[i - 1][0] + indel
        backtrack[i][0] = 'U'
    for i in range(1, ncols):
        table[0][i] = table[0][i - 1] + indel
        backtrack[0][i] = 'L'
    for i in range(1, nrows):
        for j in range(1, ncols):
            alts = (
                table[i - 1][j - 1] + scores(vstr[i - 1], ustr[j - 1]),  # pair
                table[i - 1][j] + indel,  # deletion of v[i]
                table[i][j - 1] + indel,  # inserting of w[j]
            )
            backdirs = (
                'D',
                'U',
                'L',
            )
    
            index, value = max(enumerate(alts), key=lambda x: x[1])
            table[i][j] = value
            backtrack[i][j] = backdirs[index]

    return table, backtrack


def findOGA(vstr, ustr, backtrack):
    alignment = ['', '']
    i = len(vstr)
    j = len(ustr)
    while i > 0 or j > 0:
        if backtrack[i][j] == 'U':
            i -= 1
            alignment[0] = '%s%s' % (vstr[i], alignment[0])
            alignment[1] = '-%s' % alignment[1]
        elif backtrack[i][j] == 'L':
            j -= 1
            alignment[0] = '-%s' % alignment[0]
            alignment[1] = '%s%s' % (ustr[j], alignment[1])
        else:
            i -= 1; j -= 1
            alignment[0] = '%s%s' % (vstr[i], alignment[0])
            alignment[1] = '%s%s' % (ustr[j], alignment[1])
    return alignment


def main():
    vstr = 'MOAT'
    ustr = 'BOAST'
    indel = -1
    def scores(x, y):
        ixs = { 'A': 0, 'B': 1, 'M': 2, 'O': 3, 'S': 4, 'T': 5 }
        vals = { 0: 'A', 1: 'B', 2: 'M', 3: 'O', 4: 'S', 5: 'T' }
        matrix = [
            [1, -1, -1, -2, -2, -3],
            [-1, 1, -1, -1, -2, -2],
            [-1, -1, 2, -1, -1, -2],
            [-2, -1, -1, 1, -1, -1],
            [-2, -2, -1, -1, 1, -1],
            [-3, -2, -2, -1, -1, 2],
        ]
        return matrix[ixs[x]][ixs[y]]

    # find the score matrix
    table, backtrack = sovleOGA(vstr, ustr, indel, scores)
    print 'table:'
    print2d(table, 3)
    print 'backtrack:'
    print2d(backtrack, 3)

    # find the optimal global alignment
    alignment = findOGA(vstr, ustr, backtrack)
    print 'global alignment'
    print2d(alignment, 0)

    # find the maximal score
    score = table[-1][-1]
    print 'score\n%s' % score


if __name__ == '__main__':
    main()
