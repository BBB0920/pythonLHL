# largestLandAnimals = [
#   "African Elephant",
#   "Asian Elephant",
#   "White Rhinoceros",
#   "Hippopotamus",
#   "Gaur",
#   "Giraffe"
# ]

# print(largestLandAnimals[5])
# print(largestLandAnimals[-1])
# print(largestLandAnimals[0])

# Changing the Contents of a list

# append - add to the end of the array
# insert - add at index (insert(index, "task"))
# del - delete at index (del array[index])
# + - combines two arrays into one

# Exercise: Foosball Players

foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

# Get the median player
median = int(len(foosballers)/2)
print(foosballers[median])

# Get five players in the middle
print(foosballers[median - 2 : median + 3])

# Add a fake "Average Player" to the exact middle of the list
foosballers.insert(median, "Average Player")
print(foosballers)

# Change Average Player to AVERAGE PLAYER
foosballers[median] = "AVERAGE PLAYER"
print(foosballers)

# Add five new players to the end of the list
foosballers.append("Adrian")
foosballers.append("Brian")
foosballers.append("Chris")
foosballers.append("Drew")
foosballers.append("Eric")
# Alternatively, could also do foosballers + ["Adrian", "Brian", "Chris", "Drew", "Eric"]
print(foosballers)

# Change AVERAGE PLAYER's position to middle again
del foosballers[median]
median = int(len(foosballers)/2)
foosballers.insert(median, "AVERAGE PLAYER")
print(foosballers)

# Add five more players, who are ranked, in appropriate location: 
# - Lacy is one spot ahead of Hubert
hubert = foosballers.index("Hubert")
foosballers.insert(hubert, "Lacy")
# - Omar is one spot behind Rebecca
rebecca = foosballers.index("Rebecca") + 1
foosballers.insert(rebecca, "Omar")
# - Otto is 8th best in the league
foosballers.insert(7, "Otto")
# - Chauncey is 10 spots from the bottom of the league
# print(foosballers[-1])
# print(foosballers[-2])
# print(foosballers[-3])
# print(foosballers[-4])
# print(foosballers[-5])
# print(foosballers[-6])
# print(foosballers[-7])
# print(foosballers[-8])
# print(foosballers[-9])
# print(foosballers[-10])
# foosballers.insert(-9, "Chauncey")
print(foosballers)



