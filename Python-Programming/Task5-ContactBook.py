contacts = []

def add_contact():
  name = input("Enter name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email: ")
  address = input("Enter address: ")
  contact = {"name": name, "phone": phone, "email": email, "address": address}
  contacts.append(contact)
  print("Contact added successfully!")

def view_contacts():
  if not contacts:
    print("No contacts found.")
  else:
    for contact in contacts:
      print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
  search_term = input("Enter name or phone number to search: ")
  results = []
  for contact in contacts:
    if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
      results.append(contact)
  if not results:
    print("No contacts found.")
  else:
    for contact in results:
      print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
  search_term = input("Enter name or phone number to find contact: ")
  found = False
  for i, contact in enumerate(contacts):
    if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
      print(f"Found contact: {contact['name']}")
      name = input("Enter new name (leave blank to keep current): ")
      phone = input("Enter new phone number (leave blank to keep current): ")
      email = input("Enter new email (leave blank to keep current): ")
      address = input("Enter new address (leave blank to keep current): ")
      if name:
        contacts[i]['name'] = name
      if phone:
        contacts[i]['phone'] = phone
      if email:
        contacts[i]['email'] = email
      if address:
        contacts[i]['address'] = address
      print("Contact updated successfully!")
      found = True
      break
  if not found:
    print("Contact not found.")

def delete_contact():
  search_term = input("Enter name or phone number to delete contact: ")
  found = False
  for i, contact in enumerate(contacts):
    if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
      del contacts[i]
      print("Contact deleted successfully!")
      found = True
      break
  if not found:
    print("Contact not found.")

def main():
  while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      add_contact()
    elif choice == '2':
      view_contacts()
    elif choice == '3':
      search_contact()
    elif choice == '4':
      update_contact()
    elif choice == '5':
      delete_contact()
    elif choice == '6':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
