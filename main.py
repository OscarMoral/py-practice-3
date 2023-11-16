"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random


def guess_the_number():
    target_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = int(input("Guess the number (1-10): "))
        attempts += 1

        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number ({target_number}) in {attempts} attempts.")
            break


def multiplication_table():
  number = int(input("Enter an integer: "))

  print(f"Multiplication Table for {number}:")
  # Fix code
  # implement a for loop

number = int(input("Ingresa un número:"))
print(f"Tabla de multiplicar para el número {number}:")
for i in range(1, 11):
  i = i + 1
  result = number * i 
  print(f"{number} x {i} = {result}")


def basic_calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operator == "+":
        result = num1 + num2
        print("Result:", result)
    elif operator == "-":
        result = num1 - num2
        print("Result:", result)
    elif operator == "*":
        result = num1 * num2
        print("Result:", result)
    elif operator == "/":
       
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error")
    else:
        print("Invalid operator")


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()