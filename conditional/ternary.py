food = input("Enter the food: ")
eat = "Yes" if food == "Cake" else "NO"
print(eat)

#Or clever if/ternary

age = int(input("Enter the age: "))
vote = ("No" , "Yes") [age>=18]
print(vote)