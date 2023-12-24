def add_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        'Name': name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['Name']} - {contact['Phone Number']}")

def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ")
    results = [contact for contact in contacts
               if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone Number']]
    
    if not results:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for result in results:
            print(f"{result['Name']} - {result['Phone Number']}")

def update_contact(contacts):
    name = input("Enter name of the contact to update: ")

    for contact in contacts:
        if contact['Name'] == name:
            contact['Phone Number'] = input("Enter new phone number: ")
            contact['Email'] = input("Enter new email: ")
            contact['Address'] = input("Enter new address: ")
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name of the contact to delete: ")

    for contact in contacts:
        if contact['Name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def main():
    contacts = []

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)

        elif choice == '2':
            view_contact_list(contacts)

        elif choice == '3':
            search_contact(contacts)

        elif choice == '4':
            update_contact(contacts)

        elif choice == '5':
            delete_contact(contacts)

        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
