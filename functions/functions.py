# Q1. Create a simple function that prints a message.

def greet():
    print("Hello, welcome to Python!")

greet()


# Q2. Create a function that prints your name.

def display_name():
    print("Apekshya")

display_name()


# Q3. Create a function that prints a greeting with a person's name.

def greet(name):
    print("Hello", name)

greet("Apekshya")


# Q4. Create a function that takes two numbers and adds them.

def add(a, b):
    print(a + b)

add(10, 5)


# Q5. Create a function that subtracts two numbers.

def subtract(a, b):
    print(a - b)

subtract(10, 5)


# Q6. Create a function that multiplies two numbers.

def multiply(a, b):
    print(a * b)

multiply(10, 5)


# Q7. Create a function that divides two numbers.

def divide(a, b):
    print(a / b)

divide(10, 5)


# Q8. Create a function that returns the sum of two numbers.

def add(a, b):
    return a + b

result = add(10, 5)

print(result)


# Q9. Create a function that returns the square of a number.

def square(number):
    return number ** 2

result = square(5)

print(result)


# Q10. Create a function that returns the cube of a number.

def cube(number):
    return number ** 3

result = cube(3)

print(result)


# Q11. Create a function that checks whether a number is even or odd.

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_number(10))


# Q12. Create a function that checks whether a person is eligible to vote.

def check_voting_age(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

print(check_voting_age(21))


# Q13. Create a function that returns the largest of two numbers.

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(25, 40))


# Q14. Create a function that returns the largest of three numbers.

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest(10, 25, 15))


# Q15. Create a function that calculates the average of three numbers.

def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))


# Q16. Create a function that calculates the area of a rectangle.

def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 5))


# Q17. Create a function that calculates the area of a circle.

def circle_area(radius):
    return 3.14 * radius ** 2

print(circle_area(5))


# Q18. Create a function that calculates the total price.

def total_price(price, quantity):
    return price * quantity

print(total_price(500, 3))


# Q19. Create a function that calculates the final price after discount.

def final_price(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

print(final_price(5000, 10))


# Q20. Create a function with a default parameter.

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Apekshya")


# Q21. Create a function that takes a name and age.

def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Apekshya", 21)


# Q22. Create a function that takes marks and returns the result.

def check_result(marks):
    if marks >= 40:
        return "Passed"
    else:
        return "Failed"

print(check_result(75))


# Q23. Create a function that returns a grade based on marks.

def grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

print(grade(85))


# Q24. Create a function that calculates factorial of a number.

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print(factorial(5))


# Q25. Create a function that calculates the sum of numbers from 1 to n.

def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(calculate_sum(10))


# Q26. Create a function that counts vowels in a string.

def count_vowels(text):
    count = 0

    for character in text:
        if character in "aeiou":
            count += 1

    return count

print(count_vowels("programming"))


# Q27. Create a function that finds the largest number in a list.

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

numbers = [10, 25, 7, 40, 15]

print(find_largest(numbers))


# Q28. Create a function that finds the average of numbers in a list.

def find_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]

print(find_average(numbers))


# Q29. Create a function that takes user input and checks whether
# the number is positive, negative, or zero.

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter a number: "))

print(check_number(number))


# Q30. Create a simple calculator using functions.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(add(a, b))
elif operator == "-":
    print(subtract(a, b))
elif operator == "*":
    print(multiply(a, b))
elif operator == "/":
    print(divide(a, b))
else:
    print("Invalid operator")