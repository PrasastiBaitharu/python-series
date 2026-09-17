n = int(input("Enter a number: "))
sum=0
while(n>0):
    digit = int(n%10)
    sum+=digit
    n //= 10

print("Sum is : ", sum)