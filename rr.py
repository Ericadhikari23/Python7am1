user = [
    ['ram','sita','gita','hari'],
    [1,2,3,4,5],
    ["a","b","c","d"]]

y = int(input("Enter the number to which you want to count even and odd :: "))
z = range(y+1)
for x in z:
    if x%2==0 :
        print (f"the even number is {x}")
    elif x%2!=0 :
        print(f"the odd number is {x}")
