import sys

minNumCoins = {0:0} #Dictionary 
minNumCoinsSolution = {0:[]} #Dictionary 

def DPChange(money, coins):
    for m in range(1, money + 1):
        minNumCoins[m] = 100000000
        minNumCoinsSolution[m] = []
        for i in range(0, len(coins)):
            if m >= coins[i]:
                if minNumCoins[m - coins[i]] + 1 < minNumCoins[m]: 
                    minNumCoins[m] = minNumCoins[m - coins[i]] + 1
                    minNumCoinsSolution[m] \
                        = minNumCoinsSolution[m - coins[i]] + [coins[i]]
    return (minNumCoins[money], minNumCoinsSolution[money])

coins = [1,5,10,20,25,50]
money = 100

print "PROBLEM 5"
for i in range(0, money + 1):
    print i, DPChange(i, coins)
