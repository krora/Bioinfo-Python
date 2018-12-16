#
#

from sys import maxsize as sys_maxsize


def countCoins(money, coins):
    """ rosalind.info/problems/ba5a/
        leetcode.com/articles/coin-change/
    """
    assert money > 0 \
        and money <= (sys_maxsize - 1)  # for simplicity

    def findMin(coins, rem, known):
        if rem <= 0:
            return -1
        if known[rem] is None:
            min_num = -1
            for coin in coins:
                if rem == coin:
                    min_num = 1
                    break
                res = findMin(coins, rem - coin, known)
                if res != -1 and (min_num == -1 or res < min_num):
                    min_num = 1 + res
            known[rem] = min_num
        return known[rem]

    known = [None] * (money + 1)  # +1 to shift indexes
    return findMin(coins, money, known)  # -1 if impossible


def countCoins2(money, coins):
    """ rosalind.info/problems/ba5a/
        leetcode.com/articles/coin-change/
    """
    assert money > 0 \
        and money <= (sys_maxsize - 1)  # for simplicity

    def findMin(coins, known):
        for rem in range(1, len(known)):
            min_num = -1
            for i in [rem - coin for coin in coins if coin <= rem]:
                if i == 0:
                    min_num = 1
                    break
                elif known[i] is -1:
                    pass
                elif min_num is -1 or min_num > known[i] + 1:
                    min_num = known[i] + 1
            known[rem] = min_num
        return known[-1]

    known = [None] * (money + 1)  # +1 to shift indexes
    return findMin(coins, known)  # -1 if impossible


def countCoins3(money, coins):
    """ rosalind.info/problems/ba5a/
        leetcode.com/articles/coin-change/
    """
    assert money > 0 \
        and money <= (sys_maxsize - 1)  # for simplicity

    def findMin(coins, known):
        for rem in range(1, len(known)):
            min_num = known[rem]
            for i in [rem - coin for coin in coins if coin <= rem]:
                min_num = min(min_num, known[i] + 1) if i != 0 else 1
            known[rem] = min_num
        return known[-1] if min_num < sys_maxsize else -1

    known = [sys_maxsize] * (money + 1)  # +1 to shift indexes
    return findMin(coins, known)  # -1 if impossible


def main():
    dataset = ['40', '1,5,10,20,25,50']
    money = int(dataset[0])
    coins = [int(n) for n in dataset[1].split(',')]
    assert money == 40
    assert coins == [1, 5, 10, 20, 25, 50]

    print(countCoins(money, coins))
    print(countCoins2(money, coins))
    print(countCoins3(money, coins))

    dataset = ['8074', '24,13,12,7,5,3,1']
    money = int(dataset[0])
    coins = [int(n) for n in dataset[1].split(',')]
    print(countCoins(money, coins))
    print(countCoins2(money, coins))
    print(countCoins3(money, coins))

    dataset = ['2', '24,13,12,2,1,1,1']
    money = int(dataset[0])
    coins = [int(n) for n in dataset[1].split(',')]
    print(countCoins(money, coins))
    print(countCoins2(money, coins))
    print(countCoins3(money, coins))



if __name__ == '__main__':
    main()
