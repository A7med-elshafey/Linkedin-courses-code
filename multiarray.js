var dinnerChoices = [["Salad", "Soup", "Cheese Plate"], ["Chicken", "Salmon", "Lasagna"]]
// here we called first list to appetizers and second for main dishes
let appIndex = 0
let mainDishIndex = 1
// here we difine first app to salad and sec to soup and main dish is lasagna but i want chicken so i gonna change it for my self.
let firstApp = dinnerChoices[appIndex][0]
let secondApp = dinnerChoices[appIndex][1]
let thirdMainDish = dinnerChoices[appIndex][0]
// here we print out what i difined
console.log(firstApp)
console.log(secondApp)
console.log(thirdMainDish)
// here we changed chicken to steak 
dinnerChoices[mainDishIndex][0] = "Steak"
console.log(dinnerChoices[mainDishIndex][0])
console.log(dinnerChoices)