class userAlreadyExists(Exception):
    def __init__(self, name):
        super().__init__(f'User {name} already Exists!')

class invalidPinTypeError(Exception):
    def __init__(self):
        super().__init__('Incorrect Pin entered!, pin only of Digits')

class invalidPinLenError(Exception):
    def __init__(self):
        super().__init__('Length of pin must be 4')

class incorrectEnteredPinError(Exception):
    def __init__(self):
        super().__init__("enterd pin doesn't match!")

class userNotFoundError(Exception):
    def __init__(self, name):
        super().__init__(f'The user {name} not found! First Register user!')

class invalidModeTypeError(Exception):
    def __init__(self):
        super().__init__(f'Entered Mode is invalid!, please enter a valid mode!')

class incorrectAmountInputError(Exception):
    def __init__(self):
        super().__init__(f'Entered amount is invalid!, amount is only of digits!')
        
class inSufficientBalanceError(Exception):
    def __init__(self):
        super().__init__(f'Entered amount is greater than balance, Entered amount should be smaller or equal to balance')

class InvalidUsernameError(Exception):
    def __init__(self, name):
        super().__init__(f'Enter username {name} is invalid!, username only contain alphabats')