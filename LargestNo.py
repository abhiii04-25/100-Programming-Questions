#Write a program to find the largest digit in a number n.
n=int(input("Enter an number: "))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print("The largest digit in the number is:", largest)