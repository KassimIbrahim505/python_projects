def hex_to_decimal(hex_string):
    digits = "0123456789ABCDEF"
    decimal = 0

    for char in hex_string:
        decimal = decimal * 16 + digits.index(char)

    return decimal
print(hex_to_decimal("1A3F"))  # Example usage