print ("calculation of factorial")
num = int(input("enter the number ::"))
while num<0 :
     print ("The number must be positive")
     num = int(input("enter the number again ::"))
if num == 0 :
    print ("the factorial of 0 is 1")
if num > 0 :
    for i in range(1,num+1) :
        factorial = num*i
    print (f"the factorial of {num} is {factorial}")




