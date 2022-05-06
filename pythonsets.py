from turtle import color

# in frozenset we can't add 
primarycolors = frozenset(['red', 'blue', 'yellow'])

color = "red"

if color.lower() in primarycolors:
    print(color + " is a primary color cool.")
else:
    print(color + " is not a primary color not coool.")
# new set data but not frozen so i can add.
letters = set(['a', 'b', 'c'])
letters.add('h')
print(letters)