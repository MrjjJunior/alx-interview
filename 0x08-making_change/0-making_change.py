#!/usr/bin/python3
''' making changes '''


def makeChange(coins, total):
    ''' make change '''
    # Your change is R10 , you have R5, R2 and R1 coin
    # R5 + R5 = R 10
    # R5 + R2 + R2 + R1 = 10
    # R2 x 5 = R10
    # R1 x 10 = R10
    if total < 0:
        return 0
    
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total == 0:
            break

        count += total // coin
        total = total % coin

    if total != 0:
        return -1
    
    return count
