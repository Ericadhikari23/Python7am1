#break continue and pass
''' i = 1      #(this is called the counter it starts with one
while i<=5 :
    print ("hello ",)        #we want them to print on the same line
    j = 1
    while j<=4 :
        print ("world ", end="")
        j += 1
    i +=1

# for loop
j = 0
x = "nabin"
while j<=4 :
    print (x[j])
    j +=1
dict = {"name": "eric", "age":"56" }
for k in dict:
    print (k) '''
ppp = [2345,2423,1242,1412,1341,3124,1412,1241,1241,3412,3421,1245,1242,2141]

print ("==== Welcome to the Atm of bhaktapur bank ====")
chances = 0
restart = ("y")
balance = 8500
while chances <= 4 :
    pin = int(input("Enter your pin Number :: "))
    if pin in ppp :
        print ("you have entered the pin correctly")
        print ("1. Show current balance \n2. Withdraw Cash \n3. pay in Cash \n4. Return the card")
        option = int(input("Select the operation you want to perform :: "))
        if option == 1 :
            print (f"Your balance is Rs. {balance}")
            break
        elif option ==2 :
            print ("1. 1,000 \n2. 5,000 \n3. 10,000 \n4. 50,000")
            mop = int(input("select the amount you want to withdraw"))
            while mop != 1000 or 5000 or 10000 or 50000 :
                print ("Enter the appropriate amount of balance")
                mop = int(input("select the amount you want to withdraw :: "))
            while mop > balance :
                print (f"You dont have sufficient amount in your balance to withdraw Rs. {mop}")
                mop = int(input("select the amount you want to withdraw :: "))
            print (f"please receive the amount Rs. {mop}")

        elif option ==3 :
            yy = int(input("please enter the amount of cash you want to pay in :: "))
        elif option == 4 :
            print ("print thank you for using our service")
    chances +=1












    chances += 1




