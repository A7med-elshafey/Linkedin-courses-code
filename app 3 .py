# i don't care about miles but it's ok for course.
miles = input('Enter a distance in miles: ')
# i use float because Decimal numbers.
miles_float = float(miles)
# kilometers_value = miles_value * 1.609344
kilometers = miles_float * 1.609344
print('That value in kilometers is')
print(kilometers)