rev_num=0
num =int(input("Enter a number"))
while num>0:
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10
if rev_num==num:
    print("Palindrome")
else:
    print("not palindrome")