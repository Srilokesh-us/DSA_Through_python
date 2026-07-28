# Count elements divisible by a given number
list=[10,20,30,50,60,90,300]
count=0
new_list=[]
num=int(input(" Enter the element: "))
for i in range(len(list)):
    if list[i]%num==0:
        new_list.append(list[i])
        count=count+1
print(f" Count of the elements divisible by {num} is {count}")
print(f" The divisible numbers are {new_list}")
    