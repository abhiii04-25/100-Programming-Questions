#Write a program to display all Armstrong numbers from 1 to n.
n = int(input("Enter a number: "))
print("Armstrong numbers from 1 to", n, "are:")
for num in range(1, n + 1):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == num:
        print(num)