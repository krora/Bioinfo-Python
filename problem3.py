#
#


def countBreakpoints(sequence):
    """ stepik.org/lesson/43282/step/1?unit=21346
        rosalind.info/problems/ba6b/#
    """
    length = len(sequence)
    assert length > 0
    pairs = [None] * (length + 1)
    pairs[0] = (0, sequence[0])
    pairs[-1] = (sequence[-1], length + 1)
    for i in range(length - 1):
        pairs[i + 1] = (sequence[i], (sequence[i + 1]))
    # print(pairs)

    differences = [None] * len(pairs)
    for i, pair in enumerate(pairs, start=0):
        differences[i] = pair[1] - pair[0]
    # print(differences)

    answer = 0
    for diff in differences:
        if diff != 1:
            answer += 1
    return answer


def countBreakpoints2(sequence):
    """ stepik.org/lesson/43282/step/1?unit=21346
        rosalind.info/problems/ba6b/#
    """
    npairs = len(sequence) + 1; assert (npairs) > 1
    pairs = [(0, sequence[0])]
    for i in range(npairs - 2): pairs.append( (sequence[i], (sequence[i + 1])) )
    pairs.append((sequence[-1], npairs))
    # print(pairs)

    differences = [pair[1] - pair[0] for pair in pairs]
    # print(differences)

    return npairs - differences.count(1)


def countBreakpoints3(sequence):
    """ stepik.org/lesson/43282/step/1?unit=21346
        rosalind.info/problems/ba6b/#
    """
    length = len(sequence); assert (length) > 1
    answer = 0 if sequence[0] == 1 else 1
    for i in range(length - 1):
        if sequence[i + 1] - sequence[i] != 1:
            answer += 1
    return answer + 1 if sequence[-1] != length else answer


def countBreakpoints4(sequence):
    """ stepik.org/lesson/43282/step/1?unit=21346
        rosalind.info/problems/ba6b/#
    """
    return sum(map(lambda x,y: x - y != 1,
                   sequence + [len(sequence) + 1], [0] + sequence))


def main():
    dataset = '(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'
    sequence = [int(n) for n in dataset[1:-1].split(' ')]
    assert sequence == [3, 4, 5, -12, -8, -7, -6, 1, 2, 10, 9, -11, 13, 14]

    print(countBreakpoints(sequence))
    print(countBreakpoints2(sequence))
    print(countBreakpoints3(sequence))
    print(countBreakpoints4(sequence))


if __name__ == '__main__':
    main()
