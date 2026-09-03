# String Practice

# 1. Create a string
name = "Apekshya"
print(name)

# 2. Find the length of a string
text = "Python"
print(len(text))

# 3. Access the first character
text = "Python"
print(text[0])

# 4. Access the last character
text = "Python"
print(text[-1])

# 5. Print characters using slicing
text = "Python"
print(text[0:3])

# 6. Convert string to uppercase
text = "python"
print(text.upper())

# 7. Convert string to lowercase
text = "PYTHON"
print(text.lower())

# 8. Capitalize a string
text = "python programming"
print(text.capitalize())

# 9. Count a character
text = "banana"
print(text.count("a"))

# 10. Find the position of a character
text = "Python"
print(text.find("t"))

# 11. Check if a word exists
text = "I am learning Python"
print("Python" in text)

# 12. Replace a word
text = "I like Java"
print(text.replace("Java", "Python"))

# 13. Remove spaces from the beginning and end
text = "  Python  "
print(text.strip())

# 14. Split a sentence into words
text = "I am learning Python"
print(text.split())

# 15. Join words together
words = ["I", "love", "Python"]
print(" ".join(words))

# 16. Check if string starts with a word
text = "Python programming"
print(text.startswith("Python"))

# 17. Check if string ends with a word
text = "Python programming"
print(text.endswith("programming"))

# 18. Check if string contains only numbers
text = "12345"
print(text.isdigit())

# 19. Check if string contains only letters
text = "Python"
print(text.isalpha())

# 20. Reverse a string
text = "Python"
print(text[::-1])

# 21. Print each character using a loop
text = "Python"

for char in text:
    print(char)

# 22. Count vowels
text = "programming"
count = 0

for char in text:
    if char in "aeiou":
        count += 1

print(count)

# 23. Count consonants
text = "python"
count = 0

for char in text:
    if char.isalpha() and char not in "aeiou":
        count += 1

print(count)

# 24. Count spaces
text = "I love Python"
print(text.count(" "))

# 25. Count a word in a sentence
text = "Python is easy. Python is powerful."
print(text.count("Python"))

# 26. Take a string as input
name = input("Enter your name: ")
print("Hello", name)

# 27. Convert user input to uppercase
name = input("Enter your name: ")
print(name.upper())

# 28. Check if a password has at least 8 characters
password = input("Enter password: ")

if len(password) >= 8:
    print("Valid password")
else:
    print("Password is too short")

# 29. Check whether a string is a palindrome
text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 30. Count vowels in user input
text = input("Enter a sentence: ")
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)