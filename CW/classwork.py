#add 
#sub
#multiply
#divide


number1=int(input("Enter a num:"))
number2=int(input("Enter a num:"))

def add(num1, num2):
    print(num1 + num2)

def sub(num1,num2):
    print(num1-num2)

def multi(num1, num2):
    print(num1*num2)

def divide(num1, num2):
    print(num1/num2)


add(number1, number2)
sub(number1, number2)
multi(number1, number2)
divide(number1, number2)




numb1 = int(input("Enter a num:"))
numb2 = int(input("Enter a num:"))
operator = input("Enter an operator: ")

def number(numb1, numb2):
    if operator == "+":
        print(numb1 + numb2)
    elif operator == "-":
        print(numb1 - numb2)
    elif operator == "*" :
        print(numb1 * numb2)
    elif operator == "/":
        print(numb1 / numb2)
    else:
        print("Invalid input")

number(numb1, numb2)




#The Daily Step Tracker

Steps = []
Total_steps = 0
count = 0

for i in range(7):
    Step = int(input("Enter a step: "))
    Steps.append(Step)
    Total_steps += Step
    count += 1

print(Steps)
print(Total_steps)
print(Total_steps/count)