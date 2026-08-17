# For loop is used for sequential traversing

list = [1,2,3,4,5,6,7,8,9]
for el in list:
    print(el)
else:
    print("END") #To display the final statement when the whole loop ends, it doesn't work if we use break in loops 



#range()
#Range function returns sequence of numbers, starting from 0 by default, and increments by 1 by default, and stops before a specified number

for i in range(6):
    print(i)


#pass is a null statement that does nothing. It is used as a placeholder for future code
for i in range(6):
    pass

print("END")