import json
from errors import(userAlreadyExists,
                invalidPinLenError,
                invalidPinTypeError,
                InvalidUsernameError)

class DataManagement:
    def __init__(self,filename = 'data.json'):
        self.filename = filename
        
    def readData(self):
        try:
            with open(self.filename,'r') as f:
                self.data = json.load(f)
                return self.data
        except:
            self.data = {}

    def saveData(self):
        with open(self.filename,'w') as f:
            json.dump(self.data,f,indent=4)

class UserCreation:
    def __init__(self,name,pin,balance):
        self.name = name.lower()
        self.pin = pin
        self.balance = balance
        self.userData = DataManagement()
        self.userData.readData()
    
    def addUser(self):
        try:
            if self.name in self.userData.data:
                raise userAlreadyExists(self.name)
            
            if not (self.pin).isdigit():
                raise invalidPinTypeError()
            
            if len(str(self.pin)) != 4:
                raise invalidPinLenError()
            
            if not str(self.name).isalpha():
                raise InvalidUsernameError()

            self.userData.data[self.name] = {"pin":self.pin,"balance":self.balance}
            self.userData.saveData()
        except(userAlreadyExists,
            invalidPinTypeError,
            invalidPinLenError,
            InvalidUsernameError) as e:
            print(e)
            return None