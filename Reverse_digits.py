num=int(input("enter the number"))
num=str(num)
reverse=""
for i in range(len(num)-1,-1,-1):
    reverse+=str(num[i])
print(f"sum of digits in a {num} is {reverse}")
