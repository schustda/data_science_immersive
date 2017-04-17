def find_change(coins, value):
    num = 0
    for i in sorted(coins, reverse = True):
        num += value//i
        value = value%i
    return num

if __name__ == '__main__':
    coins = [1,5,10,25]
    print (find_change(coins, 100))
    print (find_change(coins, 74))
