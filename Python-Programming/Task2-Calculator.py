def calculator():
  """A basic command-line calculator."""
  while True:
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      operator = input("Enter operator (+, -, *, /): ")

      if operator == '+':
        result = num1 + num2
      elif operator == '-':
        result = num1 - num2
      elif operator == '*':
        result = num1 * num2
      elif operator == '/':
        if num2 == 0:
          print("Error: Division by zero")
        else:
          result = num1 / num2
      else:
        print("Invalid operator")
        continue

      print("Result:", result)

      if input("Do you want to continue? (y/n): ").lower() != 'y':
          break
 
    except ValueError:
      print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
  calculator()
