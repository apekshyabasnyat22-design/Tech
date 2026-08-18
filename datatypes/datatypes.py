# Q1. Create an integer variable and print its value and type.

age = 21

print(age)
print(type(age))


# Q2. Create a float variable and print its value and type.

percentage = 95.5

print(percentage)
print(type(percentage))


# Q3. Create a string variable and print its value and type.

name = "Apekshya"

print(name)
print(type(name))


# Q4. Create a boolean variable and print its value and type.

is_student = True

print(is_student)
print(type(is_student))


# Q5. Create a variable with None and print its type.

value = None

print(value)
print(type(value))


# Q6. Create variables using different data types.

age = 21
height = 5.4
name = "Apekshya"
is_student = True

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))


# Q7. Convert a string into an integer.

number = "100"

number = int(number)

print(number)
print(type(number))



# Q8. Convert a string into a float.

number = "25.5"

number = float(number)

print(number)
print(type(number))



# Q9. Convert an integer into a string.

number = 100

number = str(number)

print(number)
print(type(number))



# Q10. Convert a float into an integer.

number = 25.8

number = int(number)

print(number)
print(type(number))



# Q11. Convert 1 and 0 into boolean values.

a = bool(1)
b = bool(0)

print(a)
print(b)



# Q12. Take a number from the user and convert it to integer.

number = input("Enter a number: ")

number = int(number)

print(number)
print(type(number))



# Q13. Find the length of a string.

name = "Apekshya"

print(len(name))



# Q14. Convert a string to uppercase.

name = "apekshya"

print(name.upper())



# Q15. Convert a string to lowercase.

name = "APEKSHYA"

print(name.lower())



# Q16. Print the first character of a string.

name = "Apekshya"

print(name[0])



# Q17. Print the last character of a string.

name = "Apekshya"

print(name[-1])



# Q18. Slice the first three characters.

name = "Apekshya"

print(name[0:3])



# Q19. Combine first name and last name.

first_name = "Apekshya"
last_name = "Basnyat"

full_name = first_name + " " + last_name

print(full_name)



# Q20. Use an f-string to display a person's age.

name = "Apekshya"
age = 21

print(f"My name is {name} and I am {age} years old.")



# Q21. Create a list of five fruits.

fruits = ["apple", "banana", "mango", "orange", "grapes"]

print(fruits)
print(type(fruits))



# Q22. Access the first item.

fruits = ["apple", "banana", "mango"]

print(fruits[0])




# Q23. Add an item to a list.

fruits = ["apple", "banana", "mango"]

fruits.append("orange")

print(fruits)




# Q24. Remove an item from a list.

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)




# Q25. Find the length of a list.

fruits = ["apple", "banana", "mango"]

print(len(fruits))




# Q26. Create a tuple.

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))




# Q27. Access an item from a tuple.

numbers = (10, 20, 30, 40)

print(numbers[1])




# Q28. Convert a tuple into a list.

numbers = (10, 20, 30, 40)

numbers = list(numbers)

print(numbers)
print(type(numbers))




# Q29. Create a set.

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))



# Q30. Create a set containing duplicate values.

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)




# Q31. Add an item to a set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)



# Q32. Convert a list into a set.

numbers = [10, 20, 20, 30, 30, 40]

numbers = set(numbers)

print(numbers)




# Q33. Create a dictionary.

student = {
    "name": "Apekshya",
    "age": 21,
    "city": "Kathmandu"
}

print(student)
print(type(student))



# Q34. Access the name.

student = {
    "name": "Apekshya",
    "age": 21,
    "city": "Kathmandu"
}

print(student["name"])



# Q35. Add a new key-value pair.

student = {
    "name": "Apekshya",
    "age": 21
}

student["course"] = "Computing"

print(student)




# Q36. Change the age.

student = {
    "name": "Apekshya",
    "age": 21
}

student["age"] = 22

print(student)



# Q37. Create a student record.

student_name = "Apekshya"       # string
age = 21                        # integer
percentage = 95.5               # float
is_student = True               # boolean
subjects = ["Python", "DBMS"]   # list
address = {
    "city": "Kathmandu"
}                               # dictionary

print(student_name)
print(age)
print(percentage)
print(is_student)
print(subjects)
print(address)



# Q38. Create a shopping item.

product = "Laptop"
price = 85000.50
quantity = 2
available = True

print(product, type(product))
print(price, type(price))
print(quantity, type(quantity))
print(available, type(available))



# Q39. Convert list -> tuple -> list.

numbers = [10, 20, 30, 40]

numbers = tuple(numbers)

print(numbers)
print(type(numbers))

numbers = list(numbers)

print(numbers)
print(type(numbers))



# Q40. Convert a number to a string.

age = 21

age = str(age)

message = "I am " + age + " years old."

print(message)



# Q41. Take student information from the user.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))
is_student = True

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Percentage:", percentage, type(percentage))
print("Student:", is_student, type(is_student))



# Q42. Create a shopping bill.

product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("Product:", product)
print("Total:", total)



# Q43. Store personal information using a dictionary.

person = {
    "name": "Apekshya",
    "age": 21,
    "city": "Kathmandu",
    "student": True
}

print(person)




# Q44. Remove duplicates from a list.

numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print(unique_numbers)




# Q45. Find the type of every item.

items = [10, 10.5, "Python", True, None]

for item in items:
    print(item, type(item))





# Q46. Create a dictionary containing a list.

student = {
    "name": "Apekshya",
    "marks": [80, 90, 85]
}

print(student)
print(student["marks"])




# Q47. Create a list containing dictionaries.

students = [
    {"name": "Apekshya", "age": 21},
    {"name": "Kunti", "age": 20},
    {"name": "Mahi", "age": 22}
]

print(students)




# Q48. Create a nested dictionary.

student = {
    "name": "Apekshya",
    "education": {
        "course": "Computing",
        "year": 4
    }
}

print(student)
print(student["education"]["course"])




# Q49. Convert user input into different data types.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print(name, type(name))
print(age, type(age))
print(height, type(height))





# Q50. Final Challenge - Student Profile

student = {
    "name": "Apekshya",
    "age": 21,
    "percentage": 95.5,
    "is_student": True,
    "subjects": ["Python", "Database", "Data Science"],
    "address": {
        "city": "Kathmandu",
        "country": "Nepal"
    }
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Percentage:", student["percentage"])
print("Student:", student["is_student"])
print("Subjects:", student["subjects"])
print("City:", student["address"]["city"])
print("Country:", student["address"]["country"])