# Q1. Create a tuple containing five fruits.

fruits = ("apple", "banana", "mango", "orange", "grapes")

print(fruits)


# Q2. Print the first item of a tuple.

fruits = ("apple", "banana", "mango")

print(fruits[0])


# Q3. Print the last item of a tuple.

fruits = ("apple", "banana", "mango")

print(fruits[-1])


# Q4. Print the second and third items of a tuple.

fruits = ("apple", "banana", "mango", "orange")

print(fruits[1])
print(fruits[2])


# Q5. Print the first three items using slicing.

fruits = ("apple", "banana", "mango", "orange", "grapes")

print(fruits[0:3])


# Q6. Print the last three items using slicing.

fruits = ("apple", "banana", "mango", "orange", "grapes")

print(fruits[-3:])


# Q7. Find the length of a tuple.

numbers = (10, 20, 30, 40, 50)

print(len(numbers))


# Q8. Check if an item exists in a tuple.

fruits = ("apple", "banana", "mango")

if "banana" in fruits:
    print("Banana is available")
else:
    print("Banana is not available")


# Q9. Count how many times a value appears in a tuple.

numbers = (10, 20, 10, 30, 10, 40)

print(numbers.count(10))


# Q10. Find the position of an item in a tuple.

fruits = ("apple", "banana", "mango", "orange")

print(fruits.index("mango"))


# Q11. Loop through a tuple and print each item.

fruits = ("apple", "banana", "mango", "orange")

for fruit in fruits:
    print(fruit)


# Q12. Loop through a tuple and print only even numbers.

numbers = (10, 15, 20, 25, 30, 35)

for number in numbers:
    if number % 2 == 0:
        print(number)


# Q13. Find the sum of numbers in a tuple.

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)

print("Total:", total)


# Q14. Find the largest number in a tuple.

numbers = (10, 25, 7, 40, 15)

print("Largest:", max(numbers))


# Q15. Find the smallest number in a tuple.

numbers = (10, 25, 7, 40, 15)

print("Smallest:", min(numbers))


# Q16. Find the average of numbers in a tuple.

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("Average:", average)


# Q17. Create a tuple with one item.

fruit = ("apple",)

print(fruit)
print(type(fruit))


# Q18. Convert a list into a tuple.

fruits = ["apple", "banana", "mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)


# Q19. Convert a tuple into a list.

fruits = ("apple", "banana", "mango")

fruits_list = list(fruits)

print(fruits_list)


# Q20. Join two tuples together.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print(combined)


# Q21. Repeat a tuple three times.

numbers = (1, 2, 3)

result = numbers * 3

print(result)


# Q22. Unpack a tuple into three variables.

person = ("Apekshya", 21, "Nepal")

name, age, country = person

print("Name:", name)
print("Age:", age)
print("Country:", country)


# Q23. Use tuple unpacking with multiple values.

numbers = (10, 20, 30, 40, 50)

a, b, *rest = numbers

print("A:", a)
print("B:", b)
print("Rest:", rest)


# Q24. Find all numbers greater than 20 in a tuple.

numbers = (10, 25, 15, 40, 30, 5)

for number in numbers:
    if number > 20:
        print(number)


# Q25. Count even and odd numbers in a tuple.

numbers = (10, 15, 20, 23, 30, 35)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)


# Q26. Find the largest and smallest numbers in a tuple.

numbers = (25, 10, 45, 5, 30)

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


# Q27. Create a tuple of student marks and check the result.

marks = (75, 85, 65, 90, 55)

average = sum(marks) / len(marks)

if average >= 40:
    print("Passed")
else:
    print("Failed")

print("Average:", average)


# Q28. Find the second largest number in a tuple.

numbers = (10, 25, 7, 40, 15)

sorted_numbers = sorted(numbers)

print("Second largest:", sorted_numbers[-2])


# Q29. Create a tuple containing student information and unpack it.

student = ("Apekshya", 21, "Computer Science", 85)

name, age, course, marks = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)


# Q30. Analyze a tuple of numbers.

numbers = (10, 15, 20, 25, 30, 35, 40)

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Total:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)