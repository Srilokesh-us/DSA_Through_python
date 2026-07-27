#Count elements greater than a given value
size=int(input("enter the size of the list"))
element_list=[]
new_list=[]
count=0

#taking the list elements from user dynamically 
print("enter elements into list")
for i in range(0,size):
    element=int(input())
    element_list.append(element)
print(f"Orginal list:{element_list}")

#counting the greater elements in the list based on the given number
element=int(input("enter the element "))
for i in range(len(element_list)):
    if element<element_list[i]:
        new_list.append(element_list[i])
        count+=1
print(f"The {element} is greater than {count} elements in the list")
print(f"Greater elements{new_list}")