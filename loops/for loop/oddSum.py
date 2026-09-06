a = []
index = 0
print("Enter a number of list: ")
for i in range(5):
    value = int(input())
    a.append(value)
    index+=1
print("Odd in the list: ")
for i in range(index):
    if(a[i]%2!=0):
        print(a[i])
