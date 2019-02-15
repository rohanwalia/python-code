#Enter number for returning list that contains elements smaller than this number
number = int(input("Enter number "))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i < number:
        b += [i]    
print(b)