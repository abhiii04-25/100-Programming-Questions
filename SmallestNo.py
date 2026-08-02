#Write a program to find the smallest digit in a number n.
n=int(input("Enter an number: "))
smallest=9
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    n=n//10
print("The smallest digit in the number is:", smallest)