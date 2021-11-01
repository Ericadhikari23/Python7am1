# print("hello")
# myname = "eric"
# group = "3b"
# print("my name {} group {}".format(myname,group))
# print (f"my name {myname} group {group}")
# agegroup = input("enter age group:")
# print(agegroup)
# p = input("enter your class : ")
# print("your class is", p, "is your class", "thus your class is",p,p,p,p )

# p = input("first number : ")
# q = input("second number : ")
# print(f"your first number is {p} your second number is {q}")
# print ("your first number is {} your second number is {}".format(p,q))


# z= 10 | 12
# print (z)
# x = int (input("enter your first number:")) balla integer ma janxa natra string ko form ma linxa python le


animals = {"mammels": "whale", "amphibian" :"frog" ,"aves" : "crow"}

a= list(animals.keys())
print (a)
print (a[1])

places = ["kalanki","banasthali","kritipur","bagbazar","basundhara"]
print (f"Welcome to Mathao select where do you want to go {places}")
print ("Our rate of charge is 20 km = Rs. 700")
x= input ("what is your desiered destination::")
while x not in places :
    print ("your destination is wrong or out of our reach please enter again")
    x = input("what is your desiered destination::")
if x == "kalanki":
    print ("kalanki is 40 km away from your current destination")
    fair1 = (40/20)*700
    print (f"Totl fair of your traval is rs. {fair1}")
    a1 = input ("Are you a student?, type yes or no::")
    if a1 == "yes" :
        print ("you will get 20% off")
        f12 = ((20/100)*(fair1))
        print (f"your new fair with discount is {f12}")
    elif a1 == "no" :
        print ("you will not get any discounts")
elif x == "banasthali":
    print ("banasthali is 65 km away from your current destination")
    fair2 = (65/20)*700
    print (f"Totl fair of your traval is rs. {fair2}")
    a2 = input ("Are you a student?, type yes or no::")
    if a2 == "yes" :
        print ("you will get 20% off")
        f22 = ((20/100)*(fair2))
        print(f"your new fair with discount is {f22}")
    elif a2 == "no" :
        print ("you will not get any discounts")
elif x == "kritipur":
    print ("kritipur is 78 km away from your current destination")
    fair3 = (78/20)*700
    print (f"Totl fair of your traval is rs. {fair3}")
    a3 = input ("Are you a student?, type yes or no::")
    if a3 == "yes" :
        print ("you will get 20% off")
        f32 = ((20/100)*(fair3))
        print(f"your new fair with discount is {f32}")
    elif a3 == "no" :
        print ("you will not get any discounts")
elif x == "bagbazar":
    print ("bagbazar is 25 km away from your current destination")
    fair4 = (25/20)*700
    print (f"Totl fair of your traval is rs. {fair4}")
    a4 = input ("Are you a student?, type yes or no::")
    if a4 == "yes" :
        print ("you will get 20% off")
        f42 = ((20/100)*(fair4))
        print(f"your new fair with discount is {f42}")
    elif a4 == "no" :
        print ("you will not get any discounts")
elif x == "basundhara":
    print ("basundhara is 6 km away from your current destination")
    fair5 = (6/20)*700
    print (f"Totl fair of your traval is rs. {fair5}")
    a5 = input ("Are you a student?, type yes or no::")
    if a5 == "yes" :
        print ("you will get 20% off")
        f52 = ((20/100)*(fair5))
        print(f"your new fair with discount is {f52}")
    elif a3 == "no" :
        print ("you will not get any discounts")
print ("thank you for using our service, please enjoy your ride")







print ("Reasult calculation of 2nd Unit test 2078")
x = input ("Enter yor Name")
y = input ("Enter your Class")
z = input ("Enter your Section")
print (f"Welcome {x} from Class {y} to your reasult calculation, please enter your marks obtained on subjects below")
nep = int(input("Enter your marks obtained in Nepali"))
eng = int(input("enter your marks obtained in English"))
math = int(input("Enter your marks obtained in Maths"))
sci = int(input("Enter your marks obtained in Science"))
pop = int(input("Enter your marks obtained in Health and population"))
while nep>100 or eng>100 or math>100 or sci>100 or pop>100:
    print ("The marks you have entered is above 100, Enter your actual marks again")
    nep = int(input("Enter your marks obtained in Nepali"))
    eng = int(input("enter your marks obtained in English"))
    math = int(input("Enter your marks obtained in Maths"))
    sci = int(input("Enter your marks obtained in Science"))
    pop = int(input("Enter your marks obtained in Health and population"))
print ("Here is the reasult you've obtained from this test")
chk= nep<35 or eng<35 or math<35 or sci<35 or pop<35
if chk :
     print ("you have failed this test")
     if nep<35:
         print (f"you have failed in nepali, Your score is only : {nep}")
     if eng < 35:
         print(f"you have failed in English, Your score is only : {eng}")
     if math < 35:
         print(f"you have failed in Math, Your score is only : {math}")
     if sci < 35:
         print(f"you have failed in Science, Your score is only: {sci}")
     if pop < 35:
         print(f"you have failed in Health and Population, Your score is only : {pop}")
else :
    print("congratulations you have passed in all subjects")
total = (nep+eng+math+sci+pop)
print (f"your total score is : {total}")
percentage = (total/5)
print (f"your percentage is : {percentage}")
if percentage<35:
    print ("You have failed so no Division")
if percentage>35 and percentage<45 :
    print ("You have got first division")
if percentage>45 and percentage<60 :
    print ("you have got second division")
if percentage>60 and percentage<75 :
    print ("good, you have got first division")
else :
    print ("Great job, You have got Distinction")

print ("good luck with your next Test")

