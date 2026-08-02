#String is immutable - We can access the value but we cannot change the value

str = "hello World"
print(str[3])

#In case of slice operator in string index out of bound error is not shown, rather than it will print till the end of the string
print(str[0:400])

print(str[0:3]) #Slicing

#In slice operator begin value of negative indexing must be higher than the end value,Otherwise it will give an empty string
print(str[-1:-3])#This will return an empty string

print(str[-3:-1]) #Negative Slicing


#string methods returns the updated string 
print(str.endswith("rld")) #It returns true or false

print(str.capitalize())#It capitalize the 1st character

print(str.replace("hello", "my"))#Replace anything

print(str.find("W")) #To find the word or character , it returns the index of the character or the first index of the word
                     # If the answer comes -1 that means it doesn't find any word 

print(str.count("hello"))