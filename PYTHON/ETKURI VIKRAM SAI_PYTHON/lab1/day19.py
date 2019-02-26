list1=[]
#print("enter character to be printed")

print("enter no of elements")
n=int(input())
for x in range(n):
    print("do u want to add number y/n")
    z=input()
    if z=='y':
        k=int(input())
        list1.append(k)
        continue
    else:
        break
print(list1)
#list2=int(list1)
for x in list1:
    count=' '
    for i in range(x):
        count=count+'*'
    print(count)

