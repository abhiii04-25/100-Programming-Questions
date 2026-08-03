#Write a program to replace all zeros in a number n with the digit 5
n=int(input("Enter a number: "))
result=0
i=1
while n>0:
    digit=n%10
    if digit==0:
        digit=5
    result=result+digit*i
    i=i*10
    n=n//10
print("The number after replacing zeros with 5 is:", result)