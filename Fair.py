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
        f12 = (fair1-(20/100)*(fair1))
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
        f22 = (fair2-(20/100)*(fair2))
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
        f32 = (fair3-(20/100)*(fair3))
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
        f42 = (fair4-(20/100)*(fair4))
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
        f52 = (fair5-(20/100)*(fair5))
        print(f"your new fair with discount is {f52}")
    elif a3 == "no" :
        print ("you will not get any discounts")
print ("thank you for using our service, please enjoy your ride")




