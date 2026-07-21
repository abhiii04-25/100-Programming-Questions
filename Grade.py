#Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).
Marks=int(input("Enter the marks of the student: "))
if(Marks>=90):
    print("A Grade")
elif(Marks>=80):
    print("B Grade")
elif(Marks>=70):
    print("C Grade")
elif(Marks>=60):
    print("D Grade")
else:
    print("Fail")