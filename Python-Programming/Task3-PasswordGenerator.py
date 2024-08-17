import random
import string

def generate_password(length, complexity):
  """Generates a random password of the specified length and complexity."""

  characters = ""
  if complexity >= 1:
    characters += string.ascii_lowercase
  if complexity >= 2:
    characters += string.ascii_uppercase
  if complexity >= 3:
    characters += string.digits
  if complexity >= 4:
    characters += string.punctuation

  if not characters:
    return "Invalid complexity level"

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():
  """Prompts the user for password length and complexity, and generates the password."""

  try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
      raise ValueError("Password length must be positive.")

    complexity = int(input("Enter the desired password complexity (1-4): "))
    if complexity < 1 or complexity > 4:
      raise ValueError("Complexity level must be between 1 and 4.")

    password = generate_password(length, complexity)
    print("Generated password:", password)
  except ValueError as e:
    print(e)

if __name__ == "__main__":
  main()
