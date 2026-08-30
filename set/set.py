# Q1. Create a set containing five fruits.

fruits = {"apple", "banana", "mango", "orange", "grapes"}

print(fruits)


# Q2. Create a set of numbers.

numbers = {10, 20, 30, 40, 50}

print(numbers)


# Q3. Create a set with duplicate values and print it.

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)


# Q4. Find the length of a set.

numbers = {10, 20, 30, 40, 50}

print(len(numbers))


# Q5. Add an item to a set.

fruits = {"apple", "banana", "mango"}

fruits.add("orange")

print(fruits)


# Q6. Add multiple items to a set.

fruits = {"apple", "banana"}

fruits.update(["mango", "orange", "grapes"])

print(fruits)


# Q7. Remove an item from a set.

fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)


# Q8. Remove an item safely using discard().

fruits = {"apple", "banana", "mango"}

fruits.discard("orange")

print(fruits)


# Q9. Check if an item exists in a set.

fruits = {"apple", "banana", "mango"}

if "apple" in fruits:
    print("Apple is available")
else:
    print("Apple is not available")


# Q10. Loop through a set and print each item.

fruits = {"apple", "banana", "mango", "orange"}

for fruit in fruits:
    print(fruit)


# Q11. Create a set of even numbers from a list.

numbers = [10, 15, 20, 23, 30, 35]

even_numbers = set()

for number in numbers:
    if number % 2 == 0:
        even_numbers.add(number)

print(even_numbers)


# Q12. Remove duplicate values from a list using a set.

numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print(unique_numbers)


# Q13. Convert a set into a list.

fruits = {"apple", "banana", "mango"}

fruit_list = list(fruits)

print(fruit_list)


# Q14. Find the union of two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)

print(result)


# Q15. Find the intersection of two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)


# Q16. Find the difference between two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)

print(result)


# Q17. Find the symmetric difference of two sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print(result)


# Q18. Check whether two sets have common items.

set1 = {"apple", "banana", "mango"}
set2 = {"mango", "orange", "grapes"}

common = set1.intersection(set2)

if common:
    print("Common items:", common)
else:
    print("No common items")


# Q19. Check whether one set is a subset of another.

set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))


# Q20. Check whether one set is a superset of another.

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}

print(set1.issuperset(set2))


# Q21. Find students who are present in both classes.

class_a = {"Ram", "Sita", "Hari", "Gita"}
class_b = {"Sita", "Gita", "John", "Maya"}

common_students = class_a.intersection(class_b)

print("Students in both classes:", common_students)


# Q22. Find students who are only in Class A.

class_a = {"Ram", "Sita", "Hari", "Gita"}
class_b = {"Sita", "Gita", "John", "Maya"}

only_a = class_a.difference(class_b)

print("Only in Class A:", only_a)


# Q23. Find all students from both classes without duplicates.

class_a = {"Ram", "Sita", "Hari"}
class_b = {"Sita", "Gita", "John"}

all_students = class_a.union(class_b)

print("All students:", all_students)


# Q24. Find common subjects between two students.

student1 = {"Python", "SQL", "Excel", "Tableau"}
student2 = {"Python", "Java", "SQL", "HTML"}

common_subjects = student1.intersection(student2)

print("Common subjects:", common_subjects)


# Q25. Find subjects studied only by the first student.

student1 = {"Python", "SQL", "Excel", "Tableau"}
student2 = {"Python", "Java", "SQL", "HTML"}

unique_subjects = student1.difference(student2)

print("Only student 1:", unique_subjects)


# Q26. Find unique numbers from two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

unique_numbers = set(list1).union(set(list2))

print(unique_numbers)


# Q27. Find numbers that appear in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_numbers = set(list1).intersection(set(list2))

print(common_numbers)


# Q28. Check whether two sets are completely different.

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets have no common items")
else:
    print("Sets have common items")


# Q29. Create a set from user input.

numbers = set()

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.add(number)

print("Unique numbers:", numbers)


# Q30. Analyze two sets of numbers.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Only in set 1:", set1.difference(set2))
print("Only in set 2:", set2.difference(set1))
print("Symmetric difference:", set1.symmetric_difference(set2))