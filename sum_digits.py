num=int(input("enter the number"))
num=str(num)
sum=0
for i in range(len(num)):
    sum+=int(num[i])
print(f"sum of digits in a {num} is {sum}")
print(type(sum))
print(type(num))