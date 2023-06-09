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

roles = [
  "Captain Malcolm Reynolds",
  "Zoe Washburn",
  "Hoban Washburn",
  "Inara Serra",
  "Jayne Cobb",
  "Kaylee Frye",
  "Dr. Simon Tam",
  "River Tam",
  "Derrial Book"
]

index = 8

for indice in range(0, index):
  print(actors[indice] + " as " + roles[indice])
