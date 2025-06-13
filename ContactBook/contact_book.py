# creating a contact book

# creating a empty dictionary to add contacts in it
contacts = {}

# creating a function which add name, number and email
def add_contacts(name,number,email):
    if name not in contacts and name == '' or email == '':
        print('please enter a valid details')
    elif name not in contacts:
        contacts[name] = {'number': number, 'email': email}
        print(f'\nNew contact is added in the book!\n')
        print(f'\nAll the contact name are here:\n\t{list(contacts.keys())}')
    else:
        print(f'the contact you want to add is already in the book with name = {name}\n')


# creating a function to see the contacts details
def contact_details(name,detail):

    if name not in contacts:
        print('the contact details your are trying to see in not in the book\n')
        return
    elif name in contacts and detail == '':
        print('Enter a vaild detail')
    elif name in contacts and detail == 'all':
        print(f'the details of the contact {name} is here :\nnumber == {contacts[name]['number']}\nemail == {contacts[name]['email']}\n')

    elif name in contacts and detail in ['email','number']:
        print(f'the {detail} detail of he contact is here:\n{detail} == {contacts[name][detail]}\n')


# creating a function to update or change the name or number or email
def update_contacts(name,detail,new_detail):

    if name not in contacts:
        print(f'the contact you want to update is not in the book!\n')
        return
    
    elif name in contacts and detail == '' or new_detail == '':
        print(f'Please enter the detail you want to update\n')
        return

    elif name in contacts and detail in ['email','number']:
            contacts[name].update({detail:new_detail})
            print(f'the give detail {detail} are updated!\n')
            print(f'\nAll the contact name are here:\n\t{list(contacts.keys())}')
    else:
        print('Enter the valid detail')


# creating a function to delete the contacts:
def delete_contacts(name):

    if name not in contacts:
        print(f'the contact {name} you tries to delete is not in the book\n')
        return
    
    elif name in contacts:
        contacts.pop(name)
        print(f'contact {name} is deleted form the book\n')
        print(f'\nAll the contact name are here:\n\t{list(contacts.keys())}')


print('Welcome to Cotact book created by Mohit Sirohi')
i = 0
while i < 1:
    print('\n1. add_contact   2.view_contact_details   3.Update_contact_details    4.delete_contact   5.Exit')

    choice = int(input('enter number for what you want to do: '))

    if choice == 1:
        name = input('\nEnter name of the contact: ')
        number = int(input('\nEnter number of the contact: '))
        email = input('\nEnter email of the contact: ')
        add_contacts(name,number,email)

    elif choice == 2:
        print(f'\nAll the contact name are here:\n\t{list(contacts.keys())}')
        name_details = input('\nEnter name of the contact: ')
        detail = input('\nEnter the detail you want to see: ')
        contact_details(name_details,detail)


    elif choice == 3:
        name_update = input('\nEnter name of the contact: ')
        detail_to_update = input('\nEnter detail you want to update: ')
        updated_detail = input('\nEnter new detail to update: ')
        update_contacts(name_update,detail_to_update,updated_detail)

    elif choice == 4:
        name_delete = input('\nEnter name you want to delete from contact book:')
        delete_contacts(name_delete)

    elif choice == 5:
        print('\nThanks for seeing contact book! see you again!')
        break

    else:
        print('\nYou choose wrong choice try again')