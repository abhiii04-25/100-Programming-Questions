#Write a program to check whether a number is a Harshad (Niven) number.
n = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(n))
if n % sum_of_digits == 0:
    print(n, "is a Harshad (Niven) number")
else:
    print(n, "is not a Harshad (Niven) number")