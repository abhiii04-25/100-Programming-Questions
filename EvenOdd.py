#Write a program to count the number of even digits and odd digits in a number n
n=int(input("Enter a number: "))
even_count=0
odd_count=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1    
    n=n//10
print("The number of even digits in the number is:", even_count)
print("The number of odd digits in the number is:", odd_count)
    