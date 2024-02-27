# Introduction to the calculator
print("Welcome to the Basic Calculator!!")
print(" ")
is_calculating = True

while is_calculating:
  # Define variables
  answer = input("Would you like to add, subtract, multiply, divide, or raise to the power? ")
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
  if answer == "add":
    print("The answer to " + str(number01) + " + " + str(number02) + " is " + str(add(number01, number02)))
  elif answer == "subtract":
    print("The answer to " + str(number01) + " - " + str(number02) + " is " + str(subtract(number01, number02)))
  elif answer == "multiply":
    print("The answer to " + str(number01) + " * " + str(number02) + " is " + str(multiply(number01, number02)))
  elif answer == "divide":
    print("The answer to " + str(number01) + " / " + str(number02) + " is " + str(divide(number01, number02)))
  elif answer == "square":
    print("The answer to " + str(number01) + " ** " + str(number02) + " is " + str(square(number01)))
  else:
    print("Please provide a valid answer")

  answer2 = input("Would you like to continue? Y/N: ")
  if answer2 == "N":
    break
  elif answer2 == "Y":
    continue
    
  

