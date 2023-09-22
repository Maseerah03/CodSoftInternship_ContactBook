# Initialize an empty contact list
contacts = []

def add_contact(name, phone, email, address):
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['Name']} - {contact['Phone']}")

def search_contact(query):
    matching_contacts = []
    for contact in contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            matching_contacts.append(contact)
    return matching_contacts

def update_contact(index, name, phone, email, address):
    if 0 < index <= len(contacts):
        contact = contacts[index - 1]
        contact['Name'] = name
        contact['Phone'] = phone
        contact['Email'] = email
        contact['Address'] = address
        print("Contact updated successfully!")
    else:
        print("Invalid contact index.")

def delete_contact(index):
    if 0 < index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        print(f"Contact '{deleted_contact['Name']}' deleted successfully!")
    else:
        print("Invalid contact index.")

# User interface
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        add_contact(name, phone, email, address)

    elif choice == "2":
        view_contact_list()

    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        matching_contacts = search_contact(query)
        if matching_contacts:
            print("Matching Contacts:")
            for index, contact in enumerate(matching_contacts, start=1):
                print(f"{index}. {contact['Name']} - {contact['Phone']}")
        else:
            print("No matching contacts found.")

    elif choice == "4":
        index = int(input("Enter the index of the contact to update: "))
        name = input("Enter updated Name: ")
        phone = input("Enter updated Phone: ")
        email = input("Enter updated Email: ")
        address = input("Enter updated Address: ")
        update_contact(index, name, phone, email, address)

    elif choice == "5":
        index = int(input("Enter the index of the contact to delete: "))
        delete_contact(index)

    elif choice == "6":
        print("Exiting Contact Management System.")
        break

    else:
        print("Invalid choice. Please select a valid option.")