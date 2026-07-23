#Find the last occurrence of an element
def lastOccurence():
    arr=[10,20,30,30,40,50,30]
    element=int(input("enter the element : "))
    for i in range((len(arr)-1),-1,-1):
        if element==arr[i]:
            return i
    return -1

def main():
    index=lastOccurence()
    print(f"element found in index {index}")
    
main()
       
       
    
