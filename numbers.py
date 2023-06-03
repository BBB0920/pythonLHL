# Introduction to Numbers
# int always rounds down to nearest whole number

# print(float(2))
# print(int(2.0))
# print(int(2.9))

# Math in Python
# a // b - This is Integer Division, where the result will be rounded down so there are no decimal places
# a ** b - This is Exponentiation (a to the power of b)

# a = 2
# b = 3
# c = 4
# print(a + b * c ** a)

# Exercise: Tax Calculator

subtotal = input("What's your subtotal? ")
taxRate = 0.25
tax = subtotal * taxRate
total = subtotal + tax
print("Your tax is " + str(tax))
print("Your total is: " + str(total))
