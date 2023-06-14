beatles = ['John', 'Paul', 'George', 'Ringo']
print(bool(beatles))
# => True
print('Axl Rose' in beatles)
# => False

beatlesWhoHaveBeenToTheMoon = []
print(bool(beatlesWhoHaveBeenToTheMoon))
# => False

shortSpeech = "I just wanted to thank everybody for everything. It's been a good whatever."
print(bool(shortSpeech))
# => True

speechless = ''
print(bool(speechless))
# => False

linesOfPythonWritten = 2688173
print(bool(linesOfPythonWritten))
# => True

timesAttackedByLions = 0
print(bool(timesAttackedByLions))
# => False

isConcidence = False
print(bool(isConcidence))
# => False

a = 10
b = 10
print(a is b)
# => True
b = 11
print(a is b)
# => False

a = 300
b = 300
print(a is b)
print(a == b)
