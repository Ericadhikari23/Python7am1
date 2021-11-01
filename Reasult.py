x=0
dd = int(input("Enter the number of students you want to make reasult of :: "))
while x<=dd :
    print("Reasult calculation of 2nd Unit test 2078")
    x = input("Enter yor Name:")
    y = input("Enter your Class:")
    z = input("Enter your Section:")
    print(f"Welcome {x} from Class {y} to your reasult calculation, please enter your marks obtained on subjects below")
    nep = int(input("Enter your marks obtained in Nepali:"))
    eng = int(input("enter your marks obtained in English:"))
    math = int(input("Enter your marks obtained in Maths:"))
    sci = int(input("Enter your marks obtained in Science:"))
    pop = int(input("Enter your marks obtained in Health and population:"))
    while nep > 100 or eng > 100 or math > 100 or sci > 100 or pop > 100:
        print("The marks you have entered is above 100, Enter your actual marks again")
        nep = int(input("Enter your marks obtained in Nepali:"))
        eng = int(input("enter your marks obtained in English:"))
        math = int(input("Enter your marks obtained in Maths:"))
        sci = int(input("Enter your marks obtained in Science:"))
        pop = int(input("Enter your marks obtained in Health and population:"))
    print("Here is the reasult you've obtained from this test:")
    chk = nep < 35 or eng < 35 or math < 35 or sci < 35 or pop < 35
    if chk:
        print("you have failed this test")
        if nep < 35:
            print(f"you have failed in nepali, Your score is only : {nep}")
        if eng < 35:
            print(f"you have failed in English, Your score is only : {eng}")
        if math < 35:
            print(f"you have failed in Math, Your score is only : {math}")
        if sci < 35:
            print(f"you have failed in Science, Your score is only: {sci}")
        if pop < 35:
            print(f"you have failed in Health and Population, Your score is only : {pop}")
    else:
        print("congratulations you have passed in all subjects")
    total = (nep + eng + math + sci + pop)
    print(f"your total score is : {total}")
    percentage = (total / 5)
    print(f"your percentage is : {percentage}")
    if percentage < 35:
        print("You have failed so no Division")
    if percentage > 35 and percentage < 45:
        print("You have got first division")
    if percentage > 45 and percentage < 60:
        print("you have got second division")
    if percentage > 60 and percentage < 75:
        print("good, you have got first division")
    if percentage > 75 :
        print("Great job, You have got Distinction")

    print("good luck with your next Test")
    x = x+1