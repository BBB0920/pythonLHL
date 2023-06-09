# Introduction to Strings

# Backslash denotes "the character immediately after me should be interpreted differently than usual"

# print("She asked, \"Can't we just leave?\" If only it were that simple.")
# print('She asked, "Can\'t we just leave?" If only it were that simple.')

# Escape characters
# https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html

# \n is new line
# print('Testing escape characters: \\n Tested "\n"')

# \a produces a beep sound
# print('Testing escape characters: \\a Tested "\a"')

# \t is tab
# print('Testing escape characters: \\t Tested "\t"')

# \v is a vertical tab - not used that often, don't worry about it
# print('Testing escape characters: \\v Tested "\v"')


# Multi-Line Strings

# veryValidString = """Hey Jude
# Don't make it bad
# Take a sad song
# And make it better"""

# print(veryValidString)


# String operations
# More available on https://docs.python.org/3/library/string.html

# firstName = "Stanislav"
# lastName = "Petrov"
# fullName = firstName + " " + lastName
# print(fullName)

# savory = "peanut butter"
# sweet = "jelly"
# sandwich = savory + " and " + sweet
# print(sandwich)

# step1 = "Eat\n"
# step2 = "Sleep\n"
# step3 = "Code\n"
# step4 = "Repeat\n"
# print(step1 + step2 + step3 + step4)

# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # second number is NOT inclusive
# print(alphabet[11:16])
# print(alphabet[:5])
# print(alphabet[20:])

# fullName = "Stanislav Petrov"
# differentName = fullName.replace("Stan", "Bob")
# print(differentName)

# Exercise: String Replacement
# Actual lyrics: 
# Just a small town girl
# Livin' in a lonely world
# She took the midnight train going anywhere
# Just a city boy
# Born and raised in South Detroit
# He took the midnight train going anywhere

journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

journey = (journey
  .replace('tone', "town")
  .replace('Leaving', "Living")
  .replace('whirl', 'world')
  .replace('tray', 'train')
  .replace('seedy', 'city')
  .replace('Bored', 'Born')
  .replace('or something', '')
)

print(journey)
