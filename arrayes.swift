var perStudentPetCount = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]
var num = perStudentPetCount.count

// print item
print(perStudentPetCount[5])

print(num)

sum = 0
for individualcount in perStudentPetCount 
{
    sum = sum + individualcount
    
}
print(sum)

var average = sum / num
print(average)