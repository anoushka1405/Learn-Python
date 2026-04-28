# Day 2 Python Mini Project: String Reversal and Sentence Case Converter
# Day 2 Python Mini Project: Text Tool

print("1. Reverse string")
print("2. Sentence case")
print("3. Uppercase")
print("4. Lowercase")
print("5. Title case")

n = int(input("Enter choice: "))

text = input("Enter string: ")

if n == 1:
    print(text[::-1])
elif n == 2:
    print(text.capitalize())
elif n == 3:
    print(text.upper())
elif n == 4:
    print(text.lower())
elif n == 5:
    print(text.title())
else:
    print("Invalid Choice!")

