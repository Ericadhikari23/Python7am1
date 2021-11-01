username = ["admin", "sophia"]
password = ["admin002", "sophia002"]
print ("=== Welcome to your account please enter your username and password")
uname = input("Enter your user name :: ")
pwrd = input("Enter your password :: ")
while uname == "admin" and pwrd == "sophia002" :
    print ("incorrect username and password")
    uname = input("Enter your user name :: ")
    pwrd = input("Enter your password :: ")
while uname == "sophia" and pwrd == "admin002" :
    print("incorrect username and password")
    uname = input("Enter your user name :: ")
    pwrd = input("Enter your password :: ")
while uname not in  username :
    print ("you have entered wrong username")
    uname = input("Enter your user name :: ")
while pwrd not in password :
    print ("you have entered wrong password")
    pwrd = input("Enter your password :: ")
print ("welcome to your account")
