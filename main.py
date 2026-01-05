from Utiliy.JSONUtils import JSONUtils

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.json_utils = JSONUtils()
        self.bank_service = BankService(self.accounts, self.json_utils)

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
                    amount = int(input("Enter amount to withdraw: "))
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

class BankService:
    def __init__(self, accounts, json_utils):
        self.accounts = accounts
        self.json_utils = json_utils

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
        user_name = input("Enter account name: ").title()
        if user_name in self.json_utils.df['name'].values:
            row_ind = self.json_utils.df.index[self.json_utils.df['name'] == user_name][0]

            new_name = input(f"\nOld Name: {self.json_utils.df.at[row_ind, 'name']} \nEnter New Name: ")
            self.json_utils.df.at[row_ind, 'name'] = new_name
            while True:
                phone = input(f"Old phone: {self.json_utils.df.at[row_ind, 'phone']} \n Enter New Phone: ")
                if len(phone) == 10 and phone.startswith(('97', '98')):
                    self.json_utils.df.at[row_ind, 'phone'] = phone
                    break
                print("Invalid phone number!")
            while True:
                new_email = input(f"Old email: {self.json_utils.df.at[row_ind, 'email']} \n Enter New Email: ")
                if new_email.endswith("@gmail.com"):
                    self.json_utils.df.at[row_ind, 'email'] = new_email
                    break
                print("Invalid Email")
            self.json_utils.df.to_json(self.json_utils.json_path, orient='records', indent=4)
            print("Account Updated Successfully")
            return
        print('Account not found')

    def delete_account(self):
        name = input("Enter account name: ").title()
        if name in self.json_utils.df['name'].values:
            self.json_utils.df = self.json_utils.df[self.json_utils.df['name'] != name]
            self.json_utils.df.to_json(self.json_utils.json_path, orient='records', indent=4)
            print(f"Account '{name}' deleted successfully!")
        else:
            print("Account not found")


def main():
    bank = BankSystem()
    bank.start_bank()


if __name__ == "__main__":
    main()
