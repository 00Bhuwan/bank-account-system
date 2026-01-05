import os
import pandas as pd

class InsufficientBalanceError(Exception):
    """"Exception raised for insufficient account balance"""
    pass

class JSONUtils:
    def __init__(self):
        self.json_path = os.path.join(os.getcwd(),'accounts.json')
        self.df = self.init_json()

    def init_json(self):
        if not os.path.exists(self.json_path):
            print(f'Creating new json file')
            empty_columns = ['name', 'balance', 'email', 'address', 'phone']
            return pd.DataFrame(columns = empty_columns)
        else:
            print(f'JSON is already created')
            return pd.read_json(self.json_path)

    def save_account(self, user_input):
        new_user = {
            'name': user_input.name,
            'balance': user_input.balance,
            'email': user_input.email,
            'address': user_input.address,
            'phone': user_input.phone
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_user])], ignore_index=True)

        self.df.to_json(self.json_path, orient='records', indent=4)

    def list_accounts(self):
        for data in self.df.to_dict(orient='records'):
            for key, value in data.items():
                print(f'{key}: {value}')
            print(f'---------------')

    def deposit(self, name, amount):
        if name in self.df['name'].values:
            self.df.loc[self.df['name'] == name, 'balance'] += amount
            print('Successfully Deposited.')
            self.df.to_json(self.json_path, orient='records', indent=4)
        else:
            print(f'Account not found.')

    def withdraw(self, name, amount):
        if name in self.df['name'].values:
            if amount > self.df.loc[self.df['name'] == name, 'balance']:
                raise InsufficientBalanceError
            else:
                self.df.loc[self.df['name'] == name, 'balance'] -= amount
                print(f'Withdraw Success')
                self.df.to_json(self.json_path, orient='records', indent=4)
        print("Account not found")