#Find the first occurrence of an element
def firstOccurence():
    arr=[10,20,30,30,40,50,30]
    element=int(input("enter the element : "))
    for i in range(len(arr)):
        if element==arr[i]:
            return i
    return -1

def main():
    index=firstOccurence()
    print(f"element found in index {index}")
    
main()
       
       
    
