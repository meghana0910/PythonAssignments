"""Answer5"""
a = 14
b = 10
if a>b :
    print("A is larger")
elif a<b :
    print("B is larger")
else:
    print("Both are equal")



"""Answer6-A2"""
a = 6
b = 5
if a % 4 == 0 and a % 3 == 0 and b % 4 == 0 and b % 3 == 0 :
    print ("Both are divisible by 4 and 3")

elif a % 4 == 0 or a % 3 ==0:
   print("A is divisible by 4 or 3")
elif b % 4 == 0 or b % 3 ==0:
   print("B is divisible by 4 or 3")
else:
    print("None of them are divisible by 4 or 3")
