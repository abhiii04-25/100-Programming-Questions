#Write a program to find the sum of all digits of a number n
n=int(input("Enter an number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("The sum of all digits from 1 to", n, "is:", sum)
