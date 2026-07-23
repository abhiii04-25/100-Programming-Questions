#Write a program to display all odd numbers from 1 to n.
n=int(input("Enter an number: "))
for i in range(1,n-1):
    if i%2==1:
        print(i)