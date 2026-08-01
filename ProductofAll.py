#Write a program to find the product of all digits of a number n
n=int(input("Enter an number: "))
product=1
for i in range(1,n+1):
    product=product*i
print("The product of all digits from 1 to", n, "is:", product)