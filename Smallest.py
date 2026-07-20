#Write a program to read three numbers and find the smallest among them.
A=int(input("Enter an number A: "))
B=int(input("Enter an number B: "))
C=int(input("Enter an number C: "))
if(A<B and A<C):
    print("A is smallest")
elif(B<A and B<C):
    print("B is smallest")
else:
    print("C is smallest")