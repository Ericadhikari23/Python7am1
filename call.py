print ("===== welcome to call cashback bonus ======")
print ("Select your service provider \n1. NTC \n2. Ncell")
caller = int(input("select your service provider::"))
reciever = int(input("select the service provider of call reciever::"))
balance = int(input("Enter your current balance in Rs."))
if caller ==1 and reciever ==1 :
    print ("you will get bonus cash back of Rs. 2.5 per 10 minute of call")
    mint = int(input("enter the Duration of your call in minute ::"))
    print (f"you will get bonus of Rs. {(2.5/10)*mint}")
    g = (2.5/10)*mint
    print("Here is the final report ::")
    print(f"Your initial balance : Rs. {balance}")
    print(f"your duration of call : {mint} minutes")
    print(f"your cashback bonus : Rs. {g}")
    print(f"your final balance : Rs. {balance + g}")
    print("Thank you for Using our service")

elif caller ==2 and reciever ==2 :
    print ("you will get bonus cash back of Rs. 5 per 10 minute of call")
    mint = int(input("enter the Duration of your call in minute ::"))
    print (f"you will get bonus of Rs. {(5/10)*mint}")
    g = (5 / 10) * mint
    print("Here is the final report ::")
    print(f"Your initial balance : Rs. {balance}")
    print(f"your duration of call : {mint} minutes")
    print(f"your cashback bonus : Rs. {g}")
    print(f"your final balance : Rs. {balance + g}")
    print("Thank you for Using our service")
else :
    print ("There wil be no cashback under this condition")
    print(f"your final balance : Rs. {balance}")

print ("Thank you for using our service")






















