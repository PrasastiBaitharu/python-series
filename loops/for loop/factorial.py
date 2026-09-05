n = int(input("Enter a number for factorial: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of the number is : ", fact)