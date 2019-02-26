def generate(x,y):
    count=''
    for i in range(x):
        count=count+y
    print(count)
print("enter number")
num1=int(input())
print("enter string")
str1=input()
generate(num1,str1)
