# Introduction to the calculator
print("======================================================================================================================")
print("- Welcome to the Basic Calculator!!")
print("- Update V1.1")
print("- IMPORTANT NOTE: When you square the number, even though it asks for 2 numbers it will just multiply the first number\nby itself, so you can type in 0 for number 2")
print("======================================================================================================================")
is_calculating = True

while is_calculating:
  # Define variables
  answer = input("Would you like to add, subtract, multiply, divide, or square? ")
  number01 = int(input("Please enter a number: "))
  number02 = int(input("Please enter another number: "))

  # Functions for equations
  def add(number01, number02):
    return number01+number02

  def subtract(number01, number02):
    return number01-number02

  def multiply(number01, number02):
    return number01*number02

  def divide(nunmber01, number02):
    return number01/number02

  def square(number01):
    return number01*number01


  # Choices
  match answer: # Pythons version of a switch statement, easier than if-else spam
    case 'add':
      print(f"The answer to: {number01} + {number02} is {add(number01,number02)}")
    case 'subtract':
      print(f"The answer to: {number01} - {number02} is {subtract(number01,number02)}")
    case 'multiply':
      print(f"The answer to: {number01} * {number02} is {multiply(number01,number02)}")
    case 'divide':
      print(f"The answer to: {number01} / {number02} is {divide(number01,number02)}")
    case 'square':
      print(f"The answer to {number01} squared is {square(number01)}")
    case other:
      print("Please provide a valid answer.")

  answer2 = input("Would you like to continue? Y/N: ")
  if answer2 == "N":
    break
  elif answer2 == "Y":
    continue
    