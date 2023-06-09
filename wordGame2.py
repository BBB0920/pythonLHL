proseString = """
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top. 

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME
"""

newProseString = proseString

# userInput = input("Please provide an exapmle of an occupation. ")
# newProseString = newProseString.replace("OCCUPATION", userInput)

# userInput = input("Please provide a country. ")
# newProseString = newProseString.replace("COUNTRY", userInput)

# userInput = input("Please provide a plural noun. ")
# newProseString = newProseString.replace("PLURAL_NOUN", userInput)

# userInput = input("Please provide a verb. ")
# newProseString = newProseString.replace("VERB", userInput)

# userInput = input("Please provide an adjective. ")
# newProseString = newProseString.replace("ADJECTIVE", userInput)

# userInput = input("Please provide an example of a personal item. ")
# newProseString = newProseString.replace("PERSONAL_ITEM", userInput)

# userInput = input("Please provide a holiday. ")
# newProseString = newProseString.replace("HOLIDAY", userInput)

# userInput = input("What is your name? ")
# newProseString = newProseString.replace("NAME", userInput)

# print(newProseString)

# Refactoring

replacements = [
  ["an occupation: ", "OCCUPATION"],
  ["a country: ", "COUNTRY"],
  ["a plural noun: ", "PLURAL_NOUN"],
  ["a verb, like 'run,' 'eat,' or 'think': ", "VERB"],
  ["an adjective, like 'friendly', 'long,' or 'warm': ", "ADJECTIVE"],
  ["a title that someone might have in an organization, like 'manager,' 'captain,' or 'trainer': ", "TITLE"],
  ["a personal item: ", "PERSONAL_ITEM"],
  ["a holiday, like Christmas or Labour Day: ", "HOLIDAY"],
  ["your name: ", "NAME"]
]

for replacement in replacements:
  prompt = "Please provide " + replacement[0]
  placeholder = replacement[1]
  userInput = input(prompt)
  newProseString = newProseString.replace(placeholder, userInput)

print(newProseString)


