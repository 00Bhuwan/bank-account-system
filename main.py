import json
from Utiliy.JSONUtils import JSONUtils

class InsufficientBalanceError(Exception):
    """"Exception raised for insufficient account balance"""
    pass

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.bank_service = BankService(self.accounts)
        self.json_utils = JSONUtils()

    def start_bank(self):
        print('Welcome to Banking Service!!')

        try:
            while True:
                user_input = int(input(
                    "\n1. Create Account\n"
                    "2. Deposit\n"
                    "3. Withdraw\n"
                    "4. View Accounts\n"
                    "5. Update Account\n"
                    "6. Delete Account\n"
                    "7. Exit\n"
                    "Enter choice: "
                ))

                if user_input == 1:
                    acc = self.bank_service.create_account()
                    self.json_utils.save_account(acc)
                    print("Account created successfully!")

                elif user_input == 2:
                    name = input("Enter account name: ").title()
                    amount = int(input("Enter amount to deposit: "))
                    self.json_utils.deposit(name, amount)

                elif user_input == 3:
                    name = input("Enter account name: ").title()
                    amount = int(input("Enter amount to deposit: "))
                    self.json_utils.withdraw(name, amount)

                elif user_input == 4:
                    self.json_utils.list_accounts()

                elif user_input == 5:
                    self.bank_service.update_account()

                elif user_input == 6:
                    self.bank_service.delete_account()

                elif user_input == 7:
                    print("Thank you for using Banking Service!")
                    break

                else:
                    print("Enter a valid option!")
        except ValueError:
            print("Enter integer value")


class BankAccount:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.balance = 0

class SavingAccount(BankAccount):
    def __init__(self):
        super().__init__(self)
        self.interest = 0.0278


class BankService:
    def __init__(self, accounts):
        self.accounts = accounts
        self.json_utils = JSONUtils()

    def create_account(self):
        name = input("Enter account name: ").title()
        address = input("Enter address: ")

        while True:
            phone = input("Enter phone number: ")
            if len(phone) == 10 and phone.startswith(("97", "98")):
                break
            for acc in self.accounts:
                if phone == acc.phone:
                    print("Account already exists")

            print("Invalid phone number!")

        while True:
            email = input("Enter email: ")
            if email.endswith("@gmail.com"):
                break
            for acc in self.accounts:
                if email == acc.email:
                    print("Account already exists")
            print("Invalid email!")

        return BankAccount(name, address, phone, email)

    def update_account(self):
        name = input("Enter account name: ").title()
        json_data = JSONUtils()
        if name in json_data.df['name'].values:
            newname = input(f"\nOld Name: {name} \nEnter New Name: ")
            if newname.strip():
                json_data.df[json_data.df["name"] == name, 'name'] = newname.title()

                while True:
                    phone = input(f"Old phone: {acc['phone']} \n Enter New Phone: ")
                    if len(phone) == 10 and phone.startswith(("97", "98")):
                        acc["phone"] = phone
                        break
                    print("Invalid phone number!")

                while True:
                    mail = input(f"Old Email: {acc['email']} \n Enter new Email: ")
                    if mail.endswith("@gmail.com"):
                        acc["email"] = mail
                        break
                    print("Invalid email!")

                print("Account updated Successfully")
                return
        print("Account Not found")

    def delete_account(self):
        name = input("Enter account name: ").title()
        json_data = self.json_utils.read_json()
        for acc in json_data:
            if acc['name'] == name:
                del acc
                print("Account deleted Successfully!")
        print("Account not found")


def main():
    bank = BankSystem()
    bank.start_bank()


if __name__ == "__main__":
    main()
