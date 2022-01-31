# Numeral System Converter

"""
TODO
1. Convert from any system to decimal
"""

def binary_to_decimal(bin_string:str) -> int:
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
    return -decimal_number if is_negative else decimal_number

def to_dec(num:int) -> int:
    pass

def main():
    print(binary_to_decimal(2))
    pass

if __name__ == "__main__":
    main()