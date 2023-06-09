# Introduction to looping
# Indentation indicates that the lines belong to non-indented line

# clothing = [
#   "Shirt",
#   "Pants",
#   "Socks"
# ]

# for item in clothing:
#   foldedItem = "Folded " + item
#   print(foldedItem)
#   print("This line is not part of the `for` loop")

# Making New Data

# instructionSteps = [
#   "turn left",
#   "go straight for 2 blocks",
#   "turn right",
#   "keep going until you see the dog statue",
#   "turn right",
#   "turn right again",
#   "park right on the sidewalk"
# ]

# instructions = "First, "

# for nextInstruction in instructionSteps:
#   instructions = instructions + nextInstruction + ", then "

# print(instructions + "you're there!")

# instructionStepsButScreemed = []

# for nextInstruction in instructionSteps:
#   upperInstruction = nextInstruction.upper()
#   instructionStepsButScreemed.append(upperInstruction)

# print(instructionStepsButScreemed)

# Iterating Over a Range

# import time

# bacteria = "🌭"
# generations = 10

# for generation in range(0, generations):
#   bacteria = bacteria * 2
#   print(bacteria)
#   time.sleep(0.5)

# Exercise: Actors

actors = [
  "Nathan Fillion",
  "Gina Torres",
  "Alan Tudyk",
  "Morena Baccarin",
  "Adam Baldwin",
  "Jewel Staite",
  "Sean Maher",
  "Summer Glau",
  "Ron Glass"
]

# roles = [
#   "Captain Malcolm Reynolds",
#   "Zoe Washburn",
#   "Hoban Washburn",
#   "Inara Serra",
#   "Jayne Cobb",
#   "Kaylee Frye",
#   "Dr. Simon Tam",
#   "River Tam",
#   "Derrial Book"
# ]

# for index in range(0, len(actors)):
#   print(actors[index] + " as " + roles[index])

# # Solution: Actors
# # Enumerate - has access to index and the item 
# for index, actor in enumerate(actors):
#   print(actor + " as " + roles[index])

# Refactor to be a List of lists

# actorRoles = [
#   ["Nathan Fillion", "Captain Malcolm Reynolds"],
#   ["Gina Torres", "Zoe Washburn"],
#   ["Alan Tudyk", "Hoban Washburn"],
#   ["Morena Baccarin", "Inara Serra"],
#   ["Adam Baldwin", "Jayne Cobb"],
#   ["Jewel Staite", "Kaylee Frye"],
#   ["Sean Maher", "Dr. Simon Tam"],
#   ["Summer Glau", "River Tam"],
#   ["Ron Glass", "Derrial Book"]
# ]

print('Featuring:\n=-=-=-=-=-=-=-=')
# for actorRole in actorRoles:
#   actor = actorRole[0]
#   role = actorRole[1]
#   print(actor + " as " + role)

# below is refactored version of the above
# for actor, role in actorRoles:
#   print(actor + " as " + role)

enumerableActors = enumerate(actors)
print(enumerableActors)
enumerableActorsList = list(enumerableActors)
print(enumerableActorsList)
