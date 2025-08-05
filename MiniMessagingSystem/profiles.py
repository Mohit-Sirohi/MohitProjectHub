from auth import*

profile_of_users = {}
def profile_set(username,name,age,school):
    if username not in logined_users:
        print('Login First!')
    else:
        profile_of_users[username] = {'name':name,'age':age,'school':school}
        print('Profile is created!')
        print(profile_of_users[username])

def profile_edit(username,password,to_change,changed):
    if username not in profile_of_users:
        print(f'There was no profile with username {username}')
    elif password != users[username]:
        print('the password which is enterd is wrong!')
    elif to_change in ('name','age','school'):
        profile_of_users[username][to_change] = changed
        print('Profiled is updated successfully')
        print(profile_of_users[username])
    else: 
        print('try again')

def delete_profile(username,password):
    if username not in profile_of_users:
        print(f'There was no profile with this username {username}')
    elif password != users[username]:
        print('The password is wrong')
    elif username not in logined_users:
        profile_of_users.pop(username)
        users.pop(username)
        print('Profile and user is deleted successfully')
    else:
        profile_of_users.pop(username)
        users.pop(username)
        logined_users.remove(username)