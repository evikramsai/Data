list1=[]
for x in range(0,10):
    print("do u want to add number y/n")
    z=input()
    if z=='y':
        k=input()
        list1.append(k)
        continue
    else:
        break
print(list1)
print("enter element to be searched")
num1=input()
if num1 in list1:
    print("true")
else:
    print("false")
