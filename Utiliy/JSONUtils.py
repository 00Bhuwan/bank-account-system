import json
import os

class JSONUtils:
    json_path = os.path.join(os.getcwd(),'accounts.json')
    def __init__(self):
        self.init_json()

    def init_json(self):
        if not os.path.exists(self.json_path):
            print(f'Creating the JSON')
            empty_array = []
            with open(self.json_path,'w') as file:
                json.dump(empty_array, file)
        else:
            print(f'JSON is Already Created')

    def read_json(self):
        json_data  = []
        with open(self.json_path, 'r', encoding='utf-8') as file:
            try:
                data_array = json.load(file)
                json_data.extend(data_array)
            except json.decoder.JSONDecodeError as json_error:
                print(f'Error in decoding the json')
        return json_data

    def save_account(self, payload):
        if os.path.exists(self.json_path):
            existing_json_data = self.read_json()
            payload_details = {
                "name" : payload.name,
                "address" : payload.address,
                "balance": payload.balance,
                "email" : payload.email,
                "phone": payload.phone
            }
            existing_json_data.append(payload_details)
            with open(self.json_path,'w') as file:
                json.dump(existing_json_data,file)
                print(f'File Dumped SuccessFully')
        return
