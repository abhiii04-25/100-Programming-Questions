#write a program to read a character and check whether it is an alphabet, digit or specia symbol.
ch = input("Enter a character: ")

if ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z':
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special Symbol")