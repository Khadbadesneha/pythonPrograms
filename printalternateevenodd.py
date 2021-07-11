
a=input("Enter the string")
i=0
b=a.split()

while i< len(b):
    if i%2==0:
        print (b[i].upper())
    else:
        print (b[i].lower())

    i=i+1
    