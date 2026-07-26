#replace negative values
list=[5,2,-3,5,7,-1]
without_neg=[]
for i in range(len(list)):
    if list[i]>0:
        without_neg.append(list[i])
    else:
        without_neg.append(0)
print(f"list without negative values :{without_neg}")
        