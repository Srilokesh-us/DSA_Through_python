#Count positive, negative, and zero elements
def main():
    arr=[10,20,-20,40,-50,0,2,3,0,-60,70,-89,200]
    pcount=0
    ncount=0
    zcount=0
    for i in range(len(arr)):
        if arr[i]>0:
            pcount+=1
        elif arr[i]<0:
            ncount+=1
        else:
            zcount+=1
    print(f"total count of positive :{pcount}, negative :{ncount} ,zeros {zcount}")
main()          