from profiles import profile_of_users

messages = {}
def send_message(by,to,text):
    if by not in profile_of_users:
        print('There was no profile with this username(Sender)')
    elif to not in profile_of_users:
        print('There was no profile with this username(Reciver)')
    else:
        if by not in messages:
            messages[by] = {to:[text]}
        else:
            if to not in messages[by].keys():
                messages[by][to] = [text]
            else:
                messages[by][to].append(text)

def view_messages(by,to):
    if by not in messages:
        print('There was no profile with this username(Sender)')
    elif to not in messages[by].keys():
        print('There was no profile with this username(Reciver)')
    else:
        print(messages[by].keys())
        if to in messages[by].keys():
            print(messages[by][to])
        elif to not in messages[by].keys():
            print(messages[by])
