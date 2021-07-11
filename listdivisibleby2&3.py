
list_output=[]
list_range = list(range(1,101,1))
for i in list_range:
    if i%2==0 and i%3==0:
        list_output.append(i)
print(list_output)

