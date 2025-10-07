import itertools as it

desc = "Converts an integer to a Roman numeral. Usage: Romanizer(<integer>)"

def Romanizer(num: int) -> str:
    num = int(num)
    if num >= 4000:
        return "The number you entered is too large. Roman Numerals can only range from 1 to 3999, and have to be a whole number. "
    
    if num <= 0:
        return "The number you entered is too small. Roman Numerals can only range from 1 to 3999, and have to be a whole number. "
   
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while num > 0:
        count = num // val[i]
        roman_num += syms[i] * count
        num -= val[i] * count
        i += 1
    return roman_num


if __name__ == '__main__':
    import sys
    try:
        print(Romanizer(int(sys.argv[1])))
    except ValueError:
        print("Invalid input. Please enter a valid integer. Roman Numerals can only range from 1 to 3999 as an integer/whole number.")
