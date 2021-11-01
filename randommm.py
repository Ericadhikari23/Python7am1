
import random
#random.random() to get random data from 0 to 1 in float
#random.uniform(1,5) to get random data from 1 to 5 in float but here 5 is non inclusive



#but we also dont use this method as we need integer not float values
# to get random integer

import randommm #dice
value1 = random.randint(1,6)   #to get random integer we use randint here both are inclusive
print (value1)

import randommm
value3 = random.randint (0,1)    #coin toss
if value3==0 :
    print ("heads")
elif value3==1 :
    print ("Tails")


#most often randint method is used

#to pick random value from a list of values we use choice function
greetings =['hi','hello','yolo','howdy']
value4 = random.choice(greetings)
print (f"{value4}, eric how are you doing")

#to get multiple random things from a list we use choices insted of choice

colours = ['red','blue','green','yellow','purple']
reasults = random.choices(colours, k=10)   # k value is how many times we want to pick a random value
print (reasults)  #this creates a list of random things of number of elements equal to k value from our initial list all are randomly selected


#we can also choose which one has higher probability to appear in the new list by adding weights function in random.choices

coloursf = ['red','blue','green']
reasults1 = random.choices(coloursf,weights=[10,10,3], k=10)
print (reasults1)  #so out of 23 red has 10 chance of appearing blue has also 10 and green has 3 least chance


#now lets see how we can randomly shuffle a list of values
deck = list(range (1,53))
random.shuffle(deck)  #we dont need any variable for this we can simply write this

print (deck)
#lets say we need to get five random cards from this deck
#we cannot use the choices method as it can randomly pick the same cards and make a list {by putting k=5} so it will not be unique cards

# so we are gonna use the sample method
# it ensures to grab only unique cards from our sample
dand = random.sample(deck, k=5)
print (dand)
#now we can pick 5 unique cards


x= 1
y= 8
z = f"the first number is {x} /n the second number is {y}"



