#
#
# https://en.wikipedia.org/wiki/Smith-Waterman_algorithm


def print2d(matr, width):
    for row in matr:
        for col in row:
            print '%*s' % (width, col),
        print


def print2dx2(matr1, matr2, width):
    for i, (row1, row2) in enumerate(zip(matr1, matr2)):
        for (col1, col2) in zip(row1, row2):
            cell = '%s,%s' %(col1, col2)
            print '%*s' % (2 * width, cell),
        print


def sovleOLA(vstr, ustr, delta): # general local alignment problem
    nrows = len(vstr) + 1
    ncols = len(ustr) + 1
    table = [[0 for j in range(ncols)] for i in range(nrows)]
    backtrack = [['' for j in range(ncols)] for i in range(nrows)]

    table[0][0] = 0
    for i in range(1, nrows):
        table[i][0] = 0
        backtrack[i][0] = 'U'
    for i in range(1, ncols):
        table[0][i] = 0
        backtrack[0][i] = 'L'
    for i in range(1, nrows):
        for j in range(1, ncols):
            alts = [
                0,                                           # free 'riding'
                table[i - 1][j] + delta(vstr[i - 1], None),  # deletion of v[i]
                table[i][j - 1] + delta(None, ustr[j - 1]),  # inserting of w[j]
                table[i - 1][j - 1] + delta(vstr[i - 1], ustr[j - 1])  # pair
            ]
            backdirs = ['R', 'U', 'L', 'D']
    
            index, value = max(enumerate(alts), key=lambda x: x[1])
            table[i][j] = value
            backtrack[i][j] = backdirs[index]

    return table, backtrack


def findOLA(vstr, ustr, table, backtrack):
    score = -1
    i = len(vstr)
    while i > 0:
        j = len(ustr)
        while j > 0:
            if table[i][j] > score:
                score = table[i][j]
                inxi, inxj = i, j
            j -= 1
        i -= 1

    alignment = ['', '', '']

    i, j = inxi, inxj
    while table[i][j] > 0:
        if backtrack[i][j] == 'R':
            raise ValueError()
        elif backtrack[i][j] == 'U':
            i -= 1
            alignment[0] = '%s%s' % (vstr[i], alignment[0])
            alignment[2] = '-%s' % alignment[2]
        elif backtrack[i][j] == 'L':
            j -= 1
            alignment[0] = '-%s' % alignment[0]
            alignment[2] = '%s%s' % (ustr[j], alignment[2])
        else:
            i -= 1; j -= 1
            alignment[0] = '%s%s' % (vstr[i], alignment[0])
            alignment[2] = '%s%s' % (ustr[j], alignment[2])

    loclen = len(alignment[0])
    indent_lft = max(i, j)
    indent_rgt = max(len(vstr) - inxi, len(ustr) - inxj)
    alignment[1] = ' ' * indent_lft + '?' * loclen + ' ' * indent_rgt
    alignment[0] = '%s%s%s' % (vstr[0:i], alignment[0], vstr[i+loclen:])
    alignment[2] = '%s%s%s' % (ustr[0:j], alignment[2], ustr[j+loclen:])
    alignment[0] = '%s%s%s' % ('#' * (j - i), alignment[0],
                               '#' * (indent_rgt - len(vstr) + inxi))
    alignment[2] = '%s%s%s' % ('#' * (i - j), alignment[2],
                               '#' * (indent_rgt - len(ustr) + inxj))

    return score, (inxi, inxj), alignment


def main():
    vstr = '1213434222'
    ustr = '1343422421'
    def delta(x, y):
        if x is None or y is None:
            return -0.5
        return 1.0 if x == y else -1.0

    # find the modified score matrix
    table, backtrack = sovleOLA(vstr, ustr, delta)
    print 'table:'
    print2d(table, 3)
    print 'backtrack:'
    print2d(backtrack, 3)
    print 'merged:'
    print2dx2(table, backtrack, 3)

    # find the optimal local alignment by score
    score, loc, alignment = findOLA(vstr, ustr, table, backtrack)
    print 'global alignment'
    print2d(alignment, 0)
    print 'score\n%s' % score
    print 'location\n%s' % str(loc)


if __name__ == '__main__':
    main()
