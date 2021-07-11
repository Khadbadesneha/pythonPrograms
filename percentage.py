"""
DS=int(input("Enter the marks"))
Micro=int(input("Enter the number"))
Al=int(input("Enter the marks"))
Java=int(input("Enter the marks"))
net=int(input("Enter the marks"))

n=(DS+Micro+Al+Java+net)*100/500

if 0<=n<40:
    print("D")
elif 40<=n<60:
    print("C")
elif 60<=n<70:
    print("B")
elif 70<=n<80:
    print("A")
elif 80<=n<100:
    print("A+")
else:
    print("invalid percentag")
"""

marks=[int(m) for m in input("Enter the number").split()]
per=sum(marks)*100/500
print(per)