import json
import os

class JsonRcds:
    """ this one manages records in json file  """

    def __init__(self):
        print('JsonRcds:init')
        self.folder_name = os.path.dirname(os.path.realpath(__file__)) #'/app/'
        self.file_name='employee_records.json'

    def test(self):
        print('JsonRcds:test ')
        self.basic_put()


    def test_return(self):
        return self.file_cwd()


    def file_cwd(self):
        print('JsonRcds:test ')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        files = os.listdir(dir_path)
        files = [f for f in files if os.path.isfile(dir_path + '/' + f)]  # Filtering only the files.
        return files

    def basic_add(self):
        print('add')
        employee_new = {'id': '03', 'name': 'Charlie', 'department': 'CEO'}
        with open(self.folder_name + self.file_name, 'r', encoding='utf-8') as f_in_obj:
            data = json.load(f_in_obj)
            # this adds the new employee to the employee record
            # data["employee"].append({
            #     "id": employee_new['id'] ,
            #     "name": employee_new['name'],
            #     "department": employee_new['department'],
            # })
            data['employee'].append(employee_new)
            self.basic_put_data(data)

    def basic_put_data(self, employee_records):
        with open(self.folder_name + self.file_name, "w", encoding='utf-8') as outfile:
            json.dump(employee_records, outfile)

    def basic_update(self, data):
        # employee_record_old={'id': '04', 'name': 'sunil', 'department': 'HR'}
        employee_record_new = {"id": "007", "name": "james", "department": "HR"}
        # del data['employee'][0]
        for employee_idx, employee_record in enumerate(data['employee']):
            if employee_record['name'] == 'Amit':
                del data['employee'][employee_idx]
        data['employee'].append(employee_record_new)
        return data

    def basic_put(self):
        # Data to be written
        employee_records = {
            "employee": [

                {
                    "id": "01",
                    "name": "Amit",
                    "department": "Sales"
                },

                {
                    "id": "04",
                    "name": "sunil",
                    "department": "HR"
                }
            ]
        }
        # Serializing json
        # json_object = json.dumps(employee_records, indent=4)
        # print(json_object)

        with open(self.folder_name + '/' + self.file_name, "w" , encoding='utf-8') as outfile:
            json.dump(employee_records, outfile)

        print('put', self.folder_name + self.file_name)

    def read_example(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = 'employee_records.json'
        print(f'c_data_json read_example dir path {dir_path} file name {file_name} ')
        return_val = ''
        # /app/algos/employee_records.json
        # /app/algos/employee_records.json

        with open('/app/employee_records.json', 'r', encoding='utf-8') as f_in_obj:
            data = json.load(f_in_obj)
            for employee_record in data['employee']:
                # print( f'c_data_json read_example {employee_record} ')
                return_val = f'JsonRcds read_example {employee_record} '
        return return_val



if __name__ == "__main__":
    c = JsonRcds()
    c.test()

