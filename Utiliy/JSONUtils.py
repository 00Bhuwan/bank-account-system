import json
import os

import pandas as pd
from numpy.ma.core import empty


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
                raise "Insufficient Balance Error"
            else:
                self.df.loc[self.df['name'] == name, 'balance'] -= amount
                print(f'Withdraw Success')
                self.df.to_json(self.json_path, orient='records', indent=4)
        print("Account not found")





            # for acc in json_data:
        #     if acc["name"] == name:
        #         amount = int(input("Enter amount to withdraw: "))
        #         if amount > acc["balance"]:
        #             raise InsufficientBalanceError
        #         else:
        #             acc["balance"] -= amount
        #             with open(self.json_utils.json_path, "w") as file:
        #                 json.dump(json_data, file, indent=4)
        #             print('withdraw success')
        #             return
        # print("Account not found!")

    # def __init__(self):
    #     self.init_json()
    #
    # def init_json(self):
    #     if not os.path.exists(self.json_path):
    #         print(f'Creating the JSON')
    #         empty_array = []
    #         with open(self.json_path,'w') as file:
    #             json.dump(empty_array, file)
    #     else:
    #         print(f'JSON is Already Created')
    #
    # def read_json(self):
    #     json_data  = []
    #     with open(self.json_path, 'r', encoding='utf-8') as file:
    #         try:
    #             data_array = json.load(file)
    #             json_data.extend(data_array)
    #         except json.decoder.JSONDecodeError as json_error:
    #             print(f'Error in decoding the json')
    #     return json_data
    #
    # def save_account(self, payload):
    #     if os.path.exists(self.json_path):
    #         existing_json_data = self.read_json()
    #         payload_details = {
    #             "name" : payload.name,
    #             "address" : payload.address,
    #             "balance": payload.balance,
    #             "email" : payload.email,
    #             "phone": payload.phone
    #         }
    #         existing_json_data.append(payload_details)
    #         with open(self.json_path,'w') as file:
    #             json.dump(existing_json_data,file)
    #             print(f'File Dumped SuccessFully')
    #     return
