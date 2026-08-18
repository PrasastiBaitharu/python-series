a = []
index = 0
print("Enter a number of list: ")
for i in range(5):
    value = int(input())
    a.append(value)
    index+=1
print("Even in the list: ")
for i in range(index-1):
    if(a[i]%2==0):
        print(a[i])
