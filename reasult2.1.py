num_of_students = int(input("Enter number of students: "))
x = 1

while x <= num_of_students:
    print(f"========Students: {x}===========")
    for a in range(1):   #yesko kam chai k
        nep = int(input("Enter your marks obtained in Nepali:"))
        eng = int(input("enter your marks obtained in English:"))
        math = int(input("Enter your marks obtained in Maths:"))
        sci = int(input("Enter your marks obtained in Science:"))
        pop = int(input("Enter your marks obtained in Health and population:"))
        nepl = []
        nepl.append(nep)
        nepl.append(eng)
        nepl.append(math)
        nepl.append(sci)
        nepl.append(pop)
        while nepl[0] > 100 or  nepl[1] > 100 or nepl[2]  > 100 or nepl[3]  > 100 or nepl[4]  > 100 :
            print("The marks you have entered is above 100, Enter your actual marks again")
            nep = int(input("Enter your marks obtained in Nepali:"))
            eng = int(input("enter your marks obtained in English:"))
            math = int(input("Enter your marks obtained in Maths:"))
            sci = int(input("Enter your marks obtained in Science:"))
            pop = int(input("Enter your marks obtained in Health and population:"))
            nepl = []
            nepl.append(nep)
            nepl.append(eng)
            nepl.append(math)
            nepl.append(sci)
            nepl.append(pop)

    print(f"======== Report of Student: {x}===========")

    if nepl[0] < 35 or  nepl[1] < 35 or nepl[2]  < 35 or nepl[3]  < 35 or nepl[4]  < 35 :
        print("you have failed this test")
        if nepl[0]  < 35:
            print(f"you have failed in nepali, Your score is only : {nep}")
        if nepl[1]  < 35:
            print(f"you have failed in English, Your score is only : {eng}")
        if nepl[2]  < 35:
            print(f"you have failed in Math, Your score is only : {math}")
        if nepl[3]  < 35:
            print(f"you have failed in Science, Your score is only: {sci}")
        if nepl[4]  < 35:
            print(f"you have failed in Health and Population, Your score is only : {pop}")
    else:
        print("congratulations you have passed in all subjects")
    total = (nepl[0] + nepl[1] + nepl[2] + nepl[3] + nepl[4])
    print(f"your total score is : {total}")
    percentage = (total / 5)
    print(f"your percentage is : {percentage}%")
    if percentage < 35:
        print("You have failed so no Division")
    if percentage > 35 and percentage < 45:
        print("You have got first division")
    if percentage > 45 and percentage < 60:
        print("you have got second division")
    if percentage > 60 and percentage < 75:
        print("good, you have got first division")
    if percentage > 75 :
        print("Good Bye")

    x += 1

