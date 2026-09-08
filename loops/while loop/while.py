count = 1
while(count<=5):
    print(count)
    count+=1

#Reverse Iteration
val = 10
while(val>=1):
    print(val)
    val-=1

#Traversing a list
list = [1,2,5,47,8,56,9,5,8,2]
i=0
while(i <= len(list)-1):
    print(list[i])
    i+=1


#search element in tuple
tup = (1,5,2,0,4,2,58,100,3,5)
num = 100
i = 0
while(i<=len(tup)-1):
    if(num == tup[i]):
        print("Got the value")
    else:
        i+=1
        continue
    i+=1