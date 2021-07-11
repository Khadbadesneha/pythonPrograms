"""
a= int(input("Enter 1st number"))
b= int(input("Enter second number"))
if a!=b:
    m=max(a,b)
    print(m)
else:
    print("NUmbers are equal")

#max between three numbers
a= int(input("Enter 1st number"))
b= int(input("Enter 2nd number"))
c= int(input("Enter 3rd number"))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("numbers are equal")
    """

#to check no is positive,negative or zero
a=int(input("enter the number"))
if a<0:
    print("number is negative")
elif a>0:
    print("number is positive")
else:
    print("number is zero")