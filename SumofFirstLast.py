#Write a program to find the sum of the first and last digit of a number n.
n=int(input("Enter a number: "))
last_digit=n%10
while n>=10:
    n=n//10
first_digit=n
sum_digits=first_digit+last_digit
print("The sum of the first and last digit is:", sum_digits)