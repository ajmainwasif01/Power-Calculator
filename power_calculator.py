
def calculate_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))


power = base**exponent
print("The raised to the power of is:" , power)
