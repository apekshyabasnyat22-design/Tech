# Q1. Check if a number is positive.

number = 10

if number > 0:
    print("Positive")


# Q2. Check if a number is negative.

number = -5

if number < 0:
    print("Negative")


# Q3. Check if a number is positive or negative.

number = -10

if number > 0:
    print("Positive")
else:
    print("Negative")


# Q4. Check if a number is even or odd.

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q5. Check if a person is eligible to vote.

age = 21

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# Q6. Check whether a student passed or failed.

marks = 65

if marks >= 40:
    print("Passed")
else:
    print("Failed")


# Q7. Check whether a number is greater than 100.

number = 150

if number > 100:
    print("Greater than 100")
else:
    print("100 or less")


# Q8. Check whether two numbers are equal.

a = 10
b = 10

if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")


# Q9. Find the greater of two numbers.

a = 25
b = 40

if a > b:
    print("A is greater")
else:
    print("B is greater")


# Q10. Check whether a person is a child, adult, or senior.

age = 65

if age < 18:
    print("Child")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# Q11. Check a student's grade.

marks = 85

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# Q12. Check whether a number is zero, positive, or negative.

number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Q13. Check if a number is divisible by 5.

number = 25

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# Q14. Check if a student passed both subjects.

math = 70
science = 65

if math >= 40 and science >= 40:
    print("Passed both subjects")
else:
    print("Failed")


# Q15. Check if a person gets a discount.

age = 65
is_member = False

if age >= 60 or is_member:
    print("Discount available")
else:
    print("No discount")


# Q16. Check whether a number is between 10 and 50.

number = 35

if number >= 10 and number <= 50:
    print("Number is in the range")
else:
    print("Number is outside the range")


# Q17. Take age from the user and check voting eligibility.

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# Q18. Take marks from the user and display pass or fail.

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Passed")
else:
    print("Failed")


# Q19. Take three numbers and find the largest.

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("A is largest")
elif b >= a and b >= c:
    print("B is largest")
else:
    print("C is largest")


# Q20. Create a simple login check.

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


# Q21. Check whether a number is a multiple of both 3 and 5.

number = 30

if number % 3 == 0 and number % 5 == 0:
    print("Multiple of both 3 and 5")
else:
    print("Not a multiple of both")


# Q22. Calculate discount based on purchase amount.

amount = 6000

if amount >= 10000:
    discount = 20
elif amount >= 5000:
    discount = 10
else:
    discount = 0

print("Discount:", discount, "%")


# Q23. Calculate the final price after discount.

price = 8000

if price >= 5000:
    discount = price * 10 / 100
else:
    discount = 0

final_price = price - discount

print("Discount:", discount)
print("Final price:", final_price)


# Q24. Check whether a student passed based on marks and attendance.

marks = 65
attendance = 80

if marks >= 40 and attendance >= 75:
    print("Student passed")
else:
    print("Student failed")


# Q25. Create a simple calculator using if-elif.

a = 20
b = 5
operator = "*"

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")


# Q26. Take a number from the user and check whether it is even,
# odd, positive, or negative.

number = int(input("Enter a number: "))

if number == 0:
    print("Zero")
elif number > 0 and number % 2 == 0:
    print("Positive even")
elif number > 0:
    print("Positive odd")
elif number % 2 == 0:
    print("Negative even")
else:
    print("Negative odd")


# Q27. Create a simple ATM withdrawal check.

balance = 10000
withdraw = 5000

if withdraw <= 0:
    print("Invalid amount")
elif withdraw > balance:
    print("Insufficient balance")
else:
    balance -= withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)


# Q28. Check whether a year is a leap year.

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Q29. Create a student result system.

marks = 78

if marks >= 80:
    print("Excellent - Grade A")
elif marks >= 60:
    print("Good - Grade B")
elif marks >= 40:
    print("Pass - Grade C")
else:
    print("Fail")


# Q30. Create a complete shopping discount system.

amount = 12000
is_member = True

if amount >= 10000 and is_member:
    discount = 20
elif amount >= 10000:
    discount = 15
elif is_member:
    discount = 10
else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Original amount:", amount)
print("Discount:", discount, "%")
print("Discount amount:", discount_amount)
print("Final amount:", final_amount)