letterHome = [
  # Title
  "A Letter Home",

  # Prose string
  """
  Hi mom,

  Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top. 

  Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

  Love,

  NAME
  """,

  # Replacements
  [
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
]

sale = [
  # Title
  "A Great Sale",

  # Prose string
  """
  SALE SALE SALE

  Today only: Buy NUMBER Plural_NOUN and get a free NOUN!

  Sign up for our exclusive METAL card and receive 50% off your first purchase!
  """,

  # Replacements
  [
    ["A number: ", "NUMBER"],
    ["A plural noun: ", "PLURAL_NOUN"],
    ["A noun: ", "NOUN"],
    ["A type of metal, such as alumninum or gold: ", "METAL"]
  ]
]

showAndTell = [
  # Title
  "Show and Tell",
  "Have you seen my pet ANIMAL? It's the best-- No pet can VERB1 as ADVERB as it can. It's NUMBER years old, and its name is NAME. YOu can VERB2 it if you want, but be careful, because it might VERB3.",

  # Replacements
  [
    ["An animal: ", "ANIMAL"],
    ["A verb, like 'run,' 'jump,' or 'cry'", "VERB1"],
    ["An adverb, like 'quickly,' 'elegantly,' or 'transparently'", "ADVERB"],
    ["A number: ", "NUMBER"],
    ['A name: ', "NAME"],
    ["A transitive verb, like 'speak to,' 'notice,' or 'touch'", "VERB2"],
    ["a verb, like 'run,' jump,' or 'cry'", "VERB3"]
  ]
]

stories = [
  letterHome,
  sale,
  showAndTell
]

print("There are " + str(len(stories)) + " stories available for you to choose. Please pick one amongst the following: ")
for index, story in enumerate(stories):
  print(str(index) + ": " + str(story[0]))

selection = input()

if int(selection) < 0 or int(selection) >= len(stories):
  print("Please make a valid selection.")
else: 
  print("You have chosen " + selection + ". " + str(stories[int(selection)][0]))
