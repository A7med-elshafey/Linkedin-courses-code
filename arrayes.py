students = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

num = len(students)

print(students[5])
print(num)
# sum and average.
sum = 0
for individual in students:
    sum = sum + individual
print(sum)
average = sum // num
print(average)