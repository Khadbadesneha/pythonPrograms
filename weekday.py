a=int(input("enter week number"))
l=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
if 0<a<=7:
    print(l[a-1])
else:
    print("Enter the number between 1to 7")
