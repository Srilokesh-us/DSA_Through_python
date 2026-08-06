#Find the GCD of 12 and 18
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd_value=gcd(12,18)
print(f"Greates common factor of 12 ,18 {gcd_value}")