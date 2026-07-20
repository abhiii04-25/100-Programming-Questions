#Write a program to read three numbers and find the largest among them.
A=int(input("Enter an number A: "))
B=int(input("Enter an number B: "))
C=int(input("Enter an number C: "))
if(A>B and A>C):
    print("A is largest")
elif(B>A and B>C):
    print("B is largest")
else:
    print("C is largest")