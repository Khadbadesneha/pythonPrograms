"""
a= int(input("ENter the number"))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print("not prime")
            break
        print("prime no")
else:
    print("not prime number")

    
a=int(input("Enter the number"))
count=0

for i in range(1,a+1):
    while (a+1)%i==0:
       count=count+1
    if count>2:
        print("not prime")
        break
    else:
        print("prime")
    
        
"""


a=int(input("Enter the number"))
count=0
for i in range(1,a+1):
    if (a+1)%i==0:
       count=count+1

if count==2:
     print("Number is Prime")
else:
    print("Number is not prime")
       
    
            

        
      
    


