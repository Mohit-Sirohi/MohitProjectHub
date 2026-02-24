from user_creation import DataManagement
from errors import (userNotFoundError,
                    invalidPinTypeError,
                    invalidPinLenError,
                    invalidModeTypeError,
                    incorrectAmountInputError,
                    inSufficientBalanceError,
                    incorrectEnteredPinError)
class Login:
    curentUser = None
    def __init__(self,name,pin):
        self.name = name.lower()
        self.pin = pin
        self.userData = DataManagement()
        self.userData.readData()

    def loginUser(self):
        try:
            if self.name not in self.userData.data:
                raise userNotFoundError(self.name)
            
            if not (self.pin).isdigit():
                raise invalidPinTypeError()
            
            if len(str(self.pin)) != 4:
                raise invalidPinLenError()
            
            if str(self.pin) != str(self.userData.data[self.name]['pin']):
                raise incorrectEnteredPinError()
            
            print(f'User {self.name} is Login!')
            Login.curentUser = self.name
        except (userNotFoundError,
                invalidPinLenError,
                invalidPinTypeError,
                incorrectEnteredPinError) as e:
            print(e)

class Mode:
    def __init__(self,mode,amount = 0):
        self.mode = mode
        self.amount = amount
        self.userData = DataManagement()
        self.userData.readData()

    def modeType(self):
        name = Login.curentUser
        try:
            if self.mode != '1' and self.mode != '2':
                raise invalidModeTypeError()
            if self.mode == '1':
                if not str(self.amount).isdigit():
                    raise incorrectAmountInputError()
                if int(self.amount) > int(self.userData.data[name]['balance']):
                    raise inSufficientBalanceError()
                amount,balance = int(self.amount),int(self.userData.data[name]['balance'])
                self.userData.data[name]['balance'] = balance - amount
                self.userData.saveData()
                print(f"Withdrawal successful! New balance: {self.userData.data[name]['balance']}")
            else:
                print(f'avaliable balance\nbalance := {self.userData.data[name]['balance']}')
        except (incorrectAmountInputError,
                    inSufficientBalanceError,
                    invalidModeTypeError) as e:
            print(e)