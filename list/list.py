# Q1. Create a list of five fruits.

fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits)


# Q2. Print the first item of a list.

fruits = ["apple", "banana", "mango"]

print(fruits[0])


# Q3. Print the last item of a list.

fruits = ["apple", "banana", "mango"]

print(fruits[-1])


# Q4. Change an item in a list.

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)


# Q5. Add an item to the end of a list.

fruits = ["apple", "banana", "mango"]

fruits.append("orange")

print(fruits)


# Q6. Add an item at a specific position.

fruits = ["apple", "banana", "mango"]

fruits.insert(1, "orange")

print(fruits)


# Q7. Add multiple items to a list.

fruits = ["apple", "banana"]

fruits.extend(["mango", "orange", "grapes"])

print(fruits)


# Q8. Remove an item from a list.

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)


# Q9. Remove the last item from a list.

fruits = ["apple", "banana", "mango"]

fruits.pop()

print(fruits)


# Q10. Find the length of a list.

numbers = [10, 20, 30, 40, 50]

print(len(numbers))


# Q11. Check if an item exists in a list.

fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is available")
else:
    print("Apple is not available")


# Q12. Print every item in a list using a loop.

fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)


# Q13. Print all numbers greater than 20.

numbers = [10, 25, 15, 40, 30, 5]

for number in numbers:
    if number > 20:
        print(number)


# Q14. Print all even numbers from a list.

numbers = [10, 15, 20, 23, 30, 35]

for number in numbers:
    if number % 2 == 0:
        print(number)


# Q15. Find the sum of all numbers in a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)


# Q16. Find the largest number in a list.

numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)


# Q17. Find the smallest number in a list.

numbers = [10, 25, 7, 40, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)


# Q18. Count the even numbers in a list.

numbers = [10, 15, 20, 23, 30, 35]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)


# Q19. Count the odd numbers in a list.

numbers = [10, 15, 20, 23, 30, 35]

count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print("Odd numbers:", count)


# Q20. Reverse a list.

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)


# Q21. Sort a list in ascending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)


# Q22. Sort a list in descending order.

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)


# Q23. Find the average of numbers in a list.

numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Average:", average)


# Q24. Create a new list containing only even numbers.

numbers = [10, 15, 20, 23, 30, 35]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# Q25. Create a new list containing only numbers greater than 50.

numbers = [20, 60, 45, 80, 30, 90]

large_numbers = []

for number in numbers:
    if number > 50:
        large_numbers.append(number)

print(large_numbers)


# Q26. Remove duplicate values from a list.

numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# Q27. Find the second largest number in a list.

numbers = [10, 25, 7, 40, 15]

numbers.sort()

print("Second largest:", numbers[-2])


# Q28. Take five numbers from the user and store them in a list.

numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("Numbers:", numbers)


# Q29. Find the total, largest, smallest, and average of a list.

numbers = [15, 25, 10, 40, 30]

total = sum(numbers)
largest = max(numbers)
smallest = min(numbers)
average = total / len(numbers)

print("Total:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)


# Q30. Create a student marks list and find the result.

marks = [75, 85, 65, 90, 55]

total = sum(marks)
average = total / len(marks)

if average >= 40:
    result = "Passed"
else:
    result = "Failed"

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Result:", result)