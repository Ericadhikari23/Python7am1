first_name= 'eric'
last_name = "adhikari"
sentence = "my name is {} {}".format (first_name, last_name) #{} are known as place holders and the value er place in the . format after writing the actual format of the sentence will get filled up in the place holders corresspondingly
print (sentence)


#but if we have a lot of place holders it will be incovinient
#now using f string

sentence1 = f"my name is {first_name} {last_name}, how are you" #f in the front to tell python that it is a f string so now we can directly add our place holders and variables in it
print (sentence1)
#convinient

#we can add function and methods directly within the f string let we have to do first name upper

sentence2 = f"my name is {first_name.upper()} {last_name.upper()}, how are you"
print (sentence2)

person = [{"name" : "eric", "age" : 23},{"name" : "gigi", "age" : 56}]
sentence6 = "my name is {} and i am {} years old".format (person[0]["name"], person[1]["age"]) #[][] nai use garna parcha to go inside a list or dictionary
print (sentence6)

sentence7 = f"My name is {person[1]['name']} \nAnd my age is {person[0]['age']}"
print (sentence7)


#we can also do calculation in module of f string
#literally everything

for n in range (1,10) :
    sentence = f"the value is {n}"
    print (sentence)


pi = 3.14159265
sentencee = f"pi is equal to {pi:.4f}"   #. denotes numbers after point 4 denotes 4 digit f means float so it will only print 4 digits after .
print (sentencee)


#if we do {pi:02} then it will be of 2 digits and 0 will be in front it is called 0 patting
