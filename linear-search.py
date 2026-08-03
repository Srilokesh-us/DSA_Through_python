#Search for an element (Linear Search)
def main():
    index=[]
    num=int(input("enter the element"))
    arr=[10,20,60,36,78,89,65,89,20,30,40,30,89,50]
    for i in range(len(arr)):
        if num==arr[i]:
            index.append(i)
    #print(f"entered number {num} is appeared in index {index}")
    print(f"Entered number {num} is found at index {', '.join(map(str, index))}")
main()  