#Write a program to count the number of factors of a number n.
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print("Number of factors of", n, "is:", count)