#.Write a program to read a character and check whether it is a vowel or a consonant.
char = input("Enter a character: ")

if char.lower() in "aeiou":
    print(char, "is a Vowel.")
else:
    print(char, "is a Consonant.")