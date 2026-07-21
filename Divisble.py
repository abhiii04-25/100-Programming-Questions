#Write a program to read a number and check whether it is divisible by both 3 and 5.
num=int(input("Enter an Number: "))
if(num%3==0):
    print("The entered number is divisible by 3: ",num)
elif(num%5==0):
    print("The entered number is divisible by 5: ",num)
else:
    print("The number is either divisible by 3 nor 5: ",num)
