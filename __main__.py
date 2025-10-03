def Roman(num):
    romanChar = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    numSplit = [[1000 for _ in range(int(num//1000))], [500 for _ in range(int(num//500))], [100 for _ in range(int(num//100))]]
    print(num%1000)
    print(numSplit)
    numeral = str(num)
    return numeral

userInput = int(input('Enter you alphanumeric number here: '))
print(f'Alphanumeric: {userInput} Roman Numeral: {Roman(userInput)}')

if __name__ == "__main__":
    import sys
    print(Roman(int(sys.argv[1])))
