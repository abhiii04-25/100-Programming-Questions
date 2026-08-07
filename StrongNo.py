#Write a program to check whether a number is a strong number (sum of factorials of its digits)
n=int(input("Enter a number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    factorial=1
    for i in range(1,digit+1):
        factorial*=i
    sum+=factorial
    temp//=10
if sum==n:
    print(n,"is a strong number")
else:
    print(n,"is not a strong number")