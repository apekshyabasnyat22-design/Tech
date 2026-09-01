# Q1. Create a dictionary containing information about a student.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student)


# Q2. Access the value of a specific key.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student["name"])


# Q3. Access a value using get().

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student.get("course"))


# Q4. Add a new key-value pair to a dictionary.

student = {
    "name": "Apekshya",
    "age": 21
}

student["city"] = "Kathmandu"

print(student)


# Q5. Change the value of an existing key.

student = {
    "name": "Apekshya",
    "age": 21
}

student["age"] = 22

print(student)


# Q6. Remove an item from a dictionary using pop().

student = {
    "name": "Apekshya",
    "age": 21,
    "city": "Kathmandu"
}

student.pop("age")

print(student)


# Q7. Delete an item using del.

student = {
    "name": "Apekshya",
    "age": 21,
    "city": "Kathmandu"
}

del student["city"]

print(student)


# Q8. Find the number of items in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(len(student))


# Q9. Print all keys in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student.keys())


# Q10. Print all values in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student.values())


# Q11. Print all key-value pairs using items().

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

print(student.items())


# Q12. Loop through all keys in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

for key in student:
    print(key)


# Q13. Loop through all values in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

for value in student.values():
    print(value)


# Q14. Loop through both keys and values.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

for key, value in student.items():
    print(key, ":", value)


# Q15. Check whether a key exists in a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "course": "Computer Science"
}

if "age" in student:
    print("Age exists")
else:
    print("Age does not exist")


# Q16. Create a dictionary of three students and their marks.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

print(marks)


# Q17. Find the marks of a particular student.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

print(marks["Apekshya"])


# Q18. Update a student's marks.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

marks["Ram"] = 80

print(marks)


# Q19. Calculate the total marks of all students.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

total = 0

for mark in marks.values():
    total += mark

print("Total:", total)


# Q20. Calculate the average marks of students.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

total = sum(marks.values())
average = total / len(marks)

print("Average:", average)


# Q21. Find the student with the highest marks.

marks = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 90
}

highest = max(marks.values())

for name, mark in marks.items():
    if mark == highest:
        print("Highest:", name, mark)


# Q22. Create a dictionary and print only values greater than 50.

marks = {
    "Apekshya": 85,
    "Ram": 45,
    "Sita": 90,
    "Hari": 35
}

for name, mark in marks.items():
    if mark > 50:
        print(name, mark)


# Q23. Create a dictionary of products and prices.

products = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000
}

print(products)


# Q24. Calculate the total price of all products.

products = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000
}

total = sum(products.values())

print("Total price:", total)


# Q25. Apply a 10% discount to all products.

products = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000
}

for product, price in products.items():
    discount = price * 10 / 100
    final_price = price - discount
    print(product, final_price)


# Q26. Create a dictionary from two lists.

names = ["Apekshya", "Ram", "Sita"]
marks = [85, 75, 90]

students = dict(zip(names, marks))

print(students)


# Q27. Count the frequency of each character in a string.

text = "banana"

frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print(frequency)


# Q28. Create a nested dictionary containing student information.

students = {
    "student1": {
        "name": "Apekshya",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "Ram",
        "age": 22,
        "marks": 75
    }
}

print(students)


# Q29. Access information from a nested dictionary.

students = {
    "student1": {
        "name": "Apekshya",
        "age": 21,
        "marks": 85
    },
    "student2": {
        "name": "Ram",
        "age": 22,
        "marks": 75
    }
}

print(students["student1"]["name"])
print(students["student1"]["marks"])


# Q30. Create a student result system using a dictionary.

students = {
    "Apekshya": 85,
    "Ram": 75,
    "Sita": 35,
    "Hari": 60
}

for name, marks in students.items():

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(name, ":", marks, "-", grade)