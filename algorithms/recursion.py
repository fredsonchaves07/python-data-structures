def factorial(number):
    if number < 0:
        raise Exception("Number invalid")
    if number == 1:
        return 1
    return number * factorial(number - 1)

print(factorial(3))
print(factorial(4))
print(factorial(6))

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(3, 2))
