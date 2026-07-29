# Print only prime numbers in the array
prime_list=[]
count=0
num=int(input("Enter the last number: "))
for i in range(2,(num+1)):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i % j==0:
            is_prime=False
            break
    if is_prime:
        prime_list.append(i)
        count=count+1

print("Prime numbers are:",prime_list)
print(f"no of prime numbers are {count}")