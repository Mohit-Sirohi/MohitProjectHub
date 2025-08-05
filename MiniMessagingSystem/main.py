from auth import login, register,logout
from profiles import profile_set,profile_edit, delete_profile
from message import send_message, view_messages

run = True
print(f'Welcome To Basic Messaging System!\n')
while run is True:
    print('Press given number to perform tasks \n')
    print('a. For login, Register or Logout\nb. create profile, edit profile or delete profile\nc. To send message or view message\n')
    command = input('Enter the alphabets here: ')
    if command == 'a':
        print('Press given number to perform tasks \n')
        print('1. Register\t2. login\t3. logout')
        command_a = int(input('Enter the number here: '))
        if command_a == 1:
            print('Registration Page\n')
            username_a1 = input('Enter your username here: ')
            password_a1 = input('Enter your password here: ')
            register(username_a1,password_a1)
        elif command_a == 2:
            print('Login page\n')
            username_a2 = input('Enter your username here: ')
            password_a2 = input('Enter your password here: ')
            login(username_a2,password_a2)
        elif command_a == 3:
            print('Logout page\n')
            username_a3 = input('Enter your username here: ')
            password_a3 = input('Enter your password here: ')
            logout(username_a3,password_a3)
    elif command == 'b':
        print('Press given number to perform tasks \n')
        print('1. Create profile\t2. Edit profile\t3. Delete profile')
        command_b = int(input('Enter the number here: '))
        if command_b == 1:
            print('Profile page\n')
            username_b1 = input('Enter your username here: ')
            name_b1 = input('Enter your name here: ')
            age_b1 = int(input('Enter your age here: '))
            school_b1 = input('Enter your school name here: ')
            profile_set(username_b1,name_b1,age_b1,school_b1)
        elif command_b == 2:
            print('Profile Edit page\n')
            username_b2 = input('Enter your username here: ')
            password_b2 = input('Enter your password here: ')
            print('Information that can be changed are 1.Name, 2.age, 3.school')
            to_change_b2 = input('Enter the Information name to change: ')
            changed_b2 = input('Enter the new information here: ')
            profile_edit(username_b2,password_b2,to_change_b2,changed_b2)
        elif command_b == 3:
            print('Profile Delete Page\n')
            username_b3 = input('Enter your username here: ')
            password_b3 = input('Enter your password here: ')
            delete_profile(username_b3,password_b3)
    elif command == 'c':
        print('Press given number to perform tasks \n')
        print('1. Send message\t2. To view message')
        command_c = int(input('Enter the number here: '))
        if command_c == 1:
            print('Messaging page\n')
            sender_c1 = input('Enter snder username here:')
            reciver_c1 = input('Enter reciver username here:')
            message_text = input('Enter your text here: ')
            send_message(sender_c1,reciver_c1,message_text)
        elif command_c ==2:
            sender_c2 = input('Enter snder username here:')
            reciver_c2 = input('Enter reciver username here:')
            view_messages(sender_c2,reciver_c2)