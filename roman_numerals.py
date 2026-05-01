def roman_numerals_converter(num): 

    # Roman Numeral Conversion 
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # Roman Numeral Storage 
    roman_numeral = ""

    for i in range (len(values)): 
        while num >= values [i]:
            roman_numeral = roman_numeral + symbols[i]
            num = num - values[i]
    return roman_numeral 

