# beatles = ['John', 'Paul', 'George', 'Ringo']
# print(bool(beatles))
# # => True
# print('Axl Rose' in beatles)
# # => False

# beatlesWhoHaveBeenToTheMoon = []
# print(bool(beatlesWhoHaveBeenToTheMoon))
# # => False

# shortSpeech = "I just wanted to thank everybody for everything. It's been a good whatever."
# print(bool(shortSpeech))
# # => True

# speechless = ''
# print(bool(speechless))
# # => False

# linesOfPythonWritten = 2688173
# print(bool(linesOfPythonWritten))
# # => True

# timesAttackedByLions = 0
# print(bool(timesAttackedByLions))
# # => False

# isConcidence = False
# print(bool(isConcidence))
# # => False

# a = 10
# b = 10
# print(a is b)
# # => True
# b = 11
# print(a is b)
# # => False

# a = 300
# b = 300
# print(a is b)
# # => Evaluates to True, but apparently this is supposed to be False?
# print(a == b)
# # => True, we want to use == instead of is

# Compound Boolean Expressions

# outsideTemperature = 28
# sunny = True
# print(outsideTemperature > 25 and sunny)
# # => True
# sunny = False
# print(outsideTemperature > 25 and sunny)
# # => False

# hasCoffee = True
# hasBeer = True
# print(hasCoffee or hasBeer)
# # => True
# hasCoffee = False
# print(hasCoffee or hasBeer)
# # => True
# print(hasCoffee and hasBeer)
# # => False

# if elif else

# cartons = [
#   ["Not almond milk", "Wrong logo"],
#   ["Not almond milk", "Wrong logo"],
#   ["Almond Milk", "Wrong logo"],
#   ["Almond Milk", "Right logo"],
#   ["Almond Milk", "Wrong logo"],
# ]

# cart = []

# wrongCartonsLookedAt = 0

# for carton in cartons:
#   typeOfMilk = carton[0]
#   logo = carton[1]
#   if typeOfMilk is "Almond Milk" and logo is "Right logo":
#     cart.append(carton)
#     break
#   else:
#     wrongCartonsLookedAt += 1

# if len(cart) is 0:
#   cart.append("Beer")

# print("I looked at " + str(wrongCartonsLookedAt) + " cartons that were not almond-painted-like-a-cow brand almond milk.")

# Else if

# age = 19

# print("Can you ride this rollercoaster?")
# if age > 18: 
#   print("Definitely!")
# elif age > 12: 
#   print("Maybe. How tall are you?")
# else:
#   print("Sorry kid, come back when you're older")

# Exercise: Password Checker

# password = "Hello"

# print("Please enter your password")
# pw = input()
# if pw == password:
#   print("That is the correct password!")
# else:
#   print("Sorry, that is incorrect.")

# Exercise: Password Validator

print("Please enter your password.")
pw = input()
print("Please input it again.")
pw2 = input()
if pw == pw2 and len(pw) >= 8:
  print("You have successfully set the password.")
elif pw != pw2:
  print("Your passwords do not match.")
elif len(pw) < 8:
  print("Your password is too short.")
