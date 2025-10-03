import itertools as it

def Romanizer(num:int):
    if num >= 4000:
        return "The number you entered is too large. Roman Numerals can only range from 1 to 3999, and have to be a whole number. "
    
    if num <= 0:
        return "The number you entered is too small. Roman Numerals can only range from 1 to 3999, and have to be a whole number. "

    romanChar = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    numSplit = []
    order = list(romanChar.keys())[-1]
    print(f'Order = {order}')
    i = 0
    for key in romanChar:
        print(f'i = {i}')
        print(f'Key = {key}')
        if num >= order:
            denom = (order for _ in range(int(num//order)))
            print(f'Denom = {denom}')
            for val in it.islice(denom, int(num//order)):
                numSplit.append(val)
            print(f'numSplit = {numSplit}')
            num = num % order
            print(f'num = {num}')
        i += 1
        if i == 7:
            break
        order = list(romanChar.keys())[-1 * (i + 1)]
        print(f'Order = {order}')
    numSplit = [romanChar.get(item, item) for item in numSplit]
    numeral = ''.join(str(item) for item in numSplit)
    print(f'Numeral = {numeral}')
    return numeral

if __name__ == '__main__':
    import sys
    print(Romanizer(int(sys.argv[1])))
