# Q1. Add two numbers.

a = 10
b = 5

print(a + b)


# Q2. Subtract two numbers.

a = 10
b = 5

print(a - b)


# Q3. Multiply two numbers.

a = 10
b = 5

print(a * b)


# Q4. Divide two numbers.

a = 10
b = 5

print(a / b)


# Q5. Find the remainder of two numbers.

a = 17
b = 5

print(a % b)


# Q6. Perform floor division on two numbers.

a = 17
b = 5

print(a // b)


# Q7. Find the power of a number.

a = 2
b = 3

print(a ** b)


# Q8. Use multiple arithmetic operators.

a = 10
b = 5
c = 2

result = a + b * c

print(result)


# Q9. Check if two numbers are equal.

a = 10
b = 10

print(a == b)


# Q10. Check if two numbers are not equal.

a = 10
b = 5

print(a != b)


# Q11. Check if one number is greater than another.

a = 10
b = 5

print(a > b)


# Q12. Check if one number is smaller than another.

a = 10
b = 5

print(a < b)


# Q13. Check if a number is greater than or equal to another number.

age = 21

print(age >= 18)


# Q14. Check if a number is smaller than or equal to another number.

age = 18

print(age <= 18)


# Q15. Use the and operator.

age = 21
is_student = True

print(age >= 18 and is_student)


# Q16. Use the or operator.

age = 16
is_student = True

print(age >= 18 or is_student)


# Q17. Use the not operator.

is_student = True

print(not is_student)


# Q18. Use the += assignment operator.

age = 21

age += 1

print(age)


# Q19. Use the -= assignment operator.

number = 10

number -= 3

print(number)


# Q20. Use the *= assignment operator.

number = 10

number *= 2

print(number)


# Q21. Use the /= assignment operator.

number = 10

number /= 2

print(number)


# Q22. Check if an item exists in a list.

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)


# Q23. Check if an item does not exist in a list.

fruits = ["apple", "banana", "mango"]

print("orange" not in fruits)


# Q24. Check whether a number is even.

number = 10

print(number % 2 == 0)


# Q25. Check whether a number is odd.

number = 7

print(number % 2 != 0)


# Q26. Calculate the total price of products.

price = 500
quantity = 3

total = price * quantity

print(total)


# Q27. Calculate the average of three numbers.

a = 10
b = 20
c = 30

average = (a + b + c) / 3

print(average)


# Q28. Calculate the area of a rectangle.

length = 10
width = 5

area = length * width

print(area)


# Q29. Calculate the remaining amount after spending money.

money = 1000
spent = 350

remaining = money - spent

print(remaining)


# Q30. Take two numbers from the user and perform arithmetic operations.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)


# Q30. Take two numbers from the user and calculate their total, difference, product, and average.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

total = a + b
difference = a - b
product = a * b
average = (a + b) / 2

print("Total:", total)
print("Difference:", difference)
print("Product:", product)
print("Average:", average)


# Q31. Calculate the total price after applying a discount.

price = 5000
discount = 10

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)


# Q32. Calculate the percentage of marks.

math = 85
science = 90
english = 80
computer = 95
database = 88

total = math + science + english + computer + database
percentage = total / 5

print("Total:", total)
print("Percentage:", percentage)


# Q33. Check whether a student passed all subjects.

math = 75
science = 65
english = 80

passed = math >= 40 and science >= 40 and english >= 40

print("Passed:", passed)


# Q34. Check whether a person is eligible to vote.

age = 21

eligible = age >= 18

print("Eligible to vote:", eligible)


# Q35. Check whether a person is eligible for a discount.

age = 65
is_member = True

eligible = age >= 60 or is_member

print("Discount available:", eligible)


# Q36. Check whether a number is between two values.

number = 50

result = number >= 10 and number <= 100

print("Number is between 10 and 100:", result)


# Q37. Check whether a number is divisible by both 3 and 5.

number = 30

result = number % 3 == 0 and number % 5 == 0

print("Divisible by both:", result)


# Q38. Calculate the remainder and check whether it is zero.

number = 25
divisor = 5

remainder = number % divisor

print("Remainder:", remainder)
print("Divisible:", remainder == 0)


# Q39. Increase a student's marks by 5 bonus marks.

marks = 75

marks += 5

print("Updated marks:", marks)


# Q40. Reduce the price by 20 percent.

price = 10000

price -= price * 20 / 100

print("Final price:", price)


# Q41. Calculate compound value using exponentiation.

principal = 10000
rate = 5
years = 2

amount = principal * (1 + rate / 100) ** years

print("Amount:", amount)


# Q42. Calculate the total cost of items with different quantities.

laptop_price = 80000
mouse_price = 1500
keyboard_price = 3000

laptop_quantity = 1
mouse_quantity = 2
keyboard_quantity = 1

total = (laptop_price * laptop_quantity) + \
        (mouse_price * mouse_quantity) + \
        (keyboard_price * keyboard_quantity)

print("Total:", total)


# Q43. Check whether a student passed based on marks and attendance.

marks = 65
attendance = 80

passed = marks >= 40 and attendance >= 75

print("Student passed:", passed)


# Q44. Check whether a person gets a discount based on age or membership.

age = 25
is_member = True

discount = age >= 60 or is_member

print("Discount available:", discount)


# Q45. Calculate the final salary after a percentage increase.

salary = 50000
increase = 10

salary += salary * increase / 100

print("New salary:", salary)


# Q46. Calculate the bill after tax.

bill = 5000
tax = 13

tax_amount = bill * tax / 100
final_bill = bill + tax_amount

print("Tax:", tax_amount)
print("Final Bill:", final_bill)


# Q47. Check whether a number is a positive even number.

number = 24

result = number > 0 and number % 2 == 0

print("Positive even number:", result)


# Q48. Check whether a number is a positive or negative number.

number = -15

positive = number > 0
negative = number < 0

print("Positive:", positive)
print("Negative:", negative)


# Q49. Calculate how many full groups can be made and how many are left.

students = 53
group_size = 5

groups = students // group_size
remaining = students % group_size

print("Full groups:", groups)
print("Remaining students:", remaining)


# Q50. Create a simple shopping bill with discount and tax.

price = 5000
quantity = 2
discount = 10
tax = 13

subtotal = price * quantity
discount_amount = subtotal * discount / 100
after_discount = subtotal - discount_amount
tax_amount = after_discount * tax / 100
final_amount = after_discount + tax_amount

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("After Discount:", after_discount)
print("Tax:", tax_amount)
print("Final Amount:", final_amount)

