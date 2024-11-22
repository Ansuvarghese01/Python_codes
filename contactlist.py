contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    number = input("Enter the contact's number: ")
    email = input("Enter the contact's email: ")
    contacts[name] = {"number": number, "email": email}
    print("Contact added successfully!")

def search_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}, Number: {contact['number']}, Email: {contact['email']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        number = input("Enter the new number: ")
        email = input("Enter the new email: ")
        contacts[name]["number"] = number
        contacts[name]["email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the contact's name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Number: {details['number']}, Email: {details['email']}")
    else:
        print("Contact list is empty.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
