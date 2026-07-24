#Write a program to find the sum of all even numbers from 1 to n.
# Input from the user
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Calculate the sum
for i in range(1, n + 1):
    total += i

# Display the result
print("Sum of natural numbers from 1 to", n, "is:", total)