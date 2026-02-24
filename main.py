from user_creation import UserCreation
from transations import Login, Mode 


def main():
    print("="*40)
    print("      WELCOME TO PYTHON ATM")
    print("="*40)

    attempts = 2

    while attempts > 0:

        print("\n1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == '1':
            name = input("Enter username: ")
            pin = input("Enter 4-digit pin: ")

            login = Login(name, pin)
            login.loginUser()

            if Login.curentUser is None:
                attempts -= 1
                print(f"Attempts left: {attempts}")
                continue

            # ---- ATM SESSION LOOP ----
            while True:
                print("\n====== ATM MENU ======")
                print("1. Withdraw")
                print("2. Balance")
                print("3. Logout")

                mode = input("Select option: ")

                if mode == '1':
                    amt = input("Enter amount: ")
                    m = Mode(mode, amt)
                    m.modeType()

                elif mode == '2':
                    m = Mode(mode)
                    m.modeType()

                elif mode == '3':
                    print("Logged out successfully!")
                    Login.curentUser = None
                    break

                else:
                    print("Invalid option!")

        elif choice == '2':
            name = input("Enter new username: ")
            pin = input("Enter 4-digit pin: ")
            bal = input("Enter starting balance: ")

            user = UserCreation(name, pin, bal)
            user.addUser()

        elif choice == '3':
            print("Thank you for using ATM 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
