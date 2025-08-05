
users = {}
def register(username,password):
    if username in users:
        print('\nThe User is already exists!\n')
    else:
        users[username] = password
        print('\nRegistration Successful\n')

logined_users = set()
def login(username,password):
    if username not in users:
        print('\nRegister yourself first!\n')
    elif password != users[username]:
        print('\nEntered password is wrong!\n')
    else:
        logined_users.add(username)
        print('\nLogin Successful\n')

def logout(username,password):
    if username not in logined_users:
        print('\nThe user is not logined\n')
    elif password != users[username]:
        print('\nThe password is wrong\n')
    else:
        logined_users.remove(username)
        print('\nyou are successfully logout\n')
