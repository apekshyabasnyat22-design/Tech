# Q1. Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)


# Q2. Print numbers from 10 to 1.

for i in range(10, 0, -1):
    print(i)


# Q3. Print even numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Q4. Print odd numbers from 1 to 20.

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# Q5. Print the multiplication table of 5.

for i in range(1, 11):
    print(5 * i)


# Q6. Print the multiplication table of a number entered by the user.

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number * i)


# Q7. Find the sum of numbers from 1 to 10.

total = 0

for i in range(1, 11):
    total += i

print(total)


# Q8. Find the sum of even numbers from 1 to 20.

total = 0

for i in range(1, 21):
    if i % 2 == 0:
        total += i

print(total)


# Q9. Print each character of a string.

name = "Apekshya"

for character in name:
    print(character)


# Q10. Print each item in a list.

fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)


# Q11. Count the number of items in a list using a loop.

fruits = ["apple", "banana", "mango", "orange"]

count = 0

for fruit in fruits:
    count += 1

print("Number of fruits:", count)


# Q12. Find the largest number in a list.

numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)


# Q13. Find the smallest number in a list.

numbers = [10, 25, 7, 40, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)


# Q14. Count how many even numbers are in a list.

numbers = [10, 15, 20, 23, 30, 35]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)


# Q15. Print numbers using a while loop.

number = 1

while number <= 10:
    print(number)
    number += 1


# Q16. Print numbers from 10 to 1 using a while loop.

number = 10

while number >= 1:
    print(number)
    number -= 1


# Q17. Find the sum of numbers from 1 to 10 using a while loop.

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Sum:", total)


# Q18. Print even numbers from 1 to 20 using a while loop.

number = 1

while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1


# Q19. Use break to stop a loop when the number reaches 5.

for i in range(1, 11):
    if i == 5:
        break
    print(i)


# Q20. Use continue to skip the number 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Q21. Find the factorial of a number.

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)


# Q22. Count the vowels in a string.

text = "programming"
count = 0

for character in text:
    if character in "aeiou":
        count += 1

print("Vowels:", count)


# Q23. Reverse a string using a loop.

text = "Python"
reverse = ""

for character in text:
    reverse = character + reverse

print(reverse)


# Q24. Check whether a number is prime.

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not prime")


# Q25. Print all prime numbers from 1 to 50.

for number in range(2, 51):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number)


# Q26. Create a simple number guessing loop.

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")


# Q27. Calculate the average of numbers in a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print("Average:", average)


# Q28. Print a multiplication table from 1 to 5.

for number in range(1, 6):
    print("Table of", number)

    for i in range(1, 11):
        print(number * i)


# Q29. Print a simple star pattern.

for i in range(1, 6):
    print("*" * i)


# Q30. Create a number analysis program.

numbers = [10, 15, 20, 25, 30, 35, 40]

even_count = 0
odd_count = 0
total = 0

for number in numbers:
    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total:", total)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)