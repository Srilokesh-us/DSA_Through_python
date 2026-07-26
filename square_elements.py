#square elements in a list
list=[1,2,3,4,5]
s_list=[]
for i in range(len(list)):
    s_list.append(list[i]*list[i])
print(f"squares of the list is : {s_list}")
    
