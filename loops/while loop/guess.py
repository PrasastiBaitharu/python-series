from random import randint

secret = randint(1,20)
count = 0
while(True):
    count+=1
    n = int(input("Enter the number: "))
    if(n==secret):
        print("You guessed it right. Number of attempt: ", count)
        break
    elif(n>secret):
        print("Too high")
        
    else:
        print("Too Low")
        


    