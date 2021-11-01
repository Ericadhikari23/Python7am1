import random
value1 = random.randint(1, 6)
print (value1)







z= random.randint(1, 20)
print ("welcome to the guessing game, if you guessed the number we are thinking you will win the Game")
x = int(input("Enter a number between 1 to 20::"))
while x>20:
    print ("you must choose a number between 1 and 20, enter again")
    x = int(input("Enter a number between 1 to 20::"))
while x != z :
    if x>z :
        print ("The number you've entered is too big")
        x = int(input("Enter a new number::"))
    elif x<z :
        print ("The number you've entered is too small")
        x = int(input("Enter a new number::"))
else :
    print ("congratulations you've made it")    #made it
PRINT (f"")