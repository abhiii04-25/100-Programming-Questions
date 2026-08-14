#Write a program to find the LCM of two numbers
def find_lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

# Example usage
num1 = 12
num2 = 18
print("The LCM of", num1, "and", num2, "is", find_lcm(num1, num2))