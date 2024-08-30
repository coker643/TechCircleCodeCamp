import json

file_path='contacts.json'
def load_contacts():
    try:
        with open(file_path,'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return{}


def save_contacts (contacts):
    with open(file_path,'w')as file:
        json.dump(contacts,file)


def add_contact(name,phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"contact'{name}'added successfully.")

def view_contacts():
    contacts = load_contacts()
    if contacts:
        print("\n---contact list ---")
        for name,phone in contacts.items():
            print(f"name:{name},phone:{phone}")
    else:
        print('no contacts found')
def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"found:{name}-{contacts[name]}")
    else:
        print(f"contact'{name}'not found.") 



while True:
    print("\nContact Book Menu")
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Quit")
    choice = input("choose an option(1-4):")

    if choice =='4':
        print("Goodbye!")
        break
    elif choice =='1':
        name = input ("Enter Name:") 
        phone = input("Enter phone number")
        add_contact(name,phone)  
    elif choice == '2':
        view_contacts()
    elif choice =='3':
        name = input("Enter the name to search:")
        search_contact(name)

    else:
        print("Invalid choice. Please try again. ")    
        

                                        
