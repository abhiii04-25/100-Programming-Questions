#Write a program to find the GCD (HCF) of two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Find the smaller number
if a < b:
    smaller = a
else:
    smaller = b

# Find the GCD
for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0):
        gcd = i

print("GCD of", a, "and", b, "is:", gcd)