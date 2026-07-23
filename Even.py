#Write a program to display all even numbers from 1 to n.
n=int(input("Enter an number: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)