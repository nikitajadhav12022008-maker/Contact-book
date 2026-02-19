##python based contact book:
##importing json and os:
import json
import os

FILE_NAME = "contacts.json"
#-------------LOAD CONTACTS-----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    return {}
#---------------SAVE CONTACTS--------------------
def save_contacts(contacts):
    with open(FILE_NAME,"w") as file:
        json.dump(contacts,file,indent=4)

#----------------ADD CONTACTS--------------------
def add_contact(contacts):
    name = input("Enter name:").title()

    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone:")
    email = input("Enter email:")
    contacts[name] = {"phone":phone,"email":email}
    save_contacts(contacts)
    print("Contact added successfully!")

#------------VIEW CONTACTS------------
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"{name} | {info['phone']} | {info['email']}")

-------------SEARCH CONTACTS-------------
def search_contact(contacts):
    name = input("Enter name to search: ").title()

    if name in contacts:
        info = contacts[name]
        print(f"\n{name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("Contact not found.")


#------------UPDATE CONTACTS-----------
def update_contact(contacts):
    name = input("Enter contact to update: ").title()

    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")

        contacts[name] = {"phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact updated!")
    else:
        print("Contact not found.")

#--------------DELETE CONTACTS--------------
def delete_contact(contacts):
    name = input("Enter contact to delete: ").title()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted!")
    else:
        print("Contact not found.")

#--------------MAIN MENU-----------------
def main():
    contacts = load_contacts()

    while True:
        print("\n==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

