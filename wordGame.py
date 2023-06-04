print("Here is my story")
story = "Just as I arrived at (Place), I realized I had forgotten my (Object)."
print(story)
print("Please fill in the blank with your own words!")

place = input("Tell me a place: ")
obj = input("Now give me an object: ")

story = (story
  .replace("(Place)", place)
  .replace("(Object)", obj)
)

print(story)
