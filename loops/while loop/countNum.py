n = int(input("Enter a number: "))
count = 0
evenCount = 0
while(n>0):
    digit = int(n%10)
    count+=1
    if(digit%2==0):
        evenCount+=1
    n //= 10
print("Total number of digits are: ", count)
print("Total number of even number: ", evenCount)