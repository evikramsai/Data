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
n=int(input())
for x in list1:
    y=len(x)
    if y>n:
        print(x)
