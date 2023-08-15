import json
import os
from datetime import datetime


class cDataTask:
    """
    This will manage the JSON data to file
    ECHO adding Germany to Country here.
    curl --json @country.json https://basicwebemployee-i4sibuqq3a-ul.a.run.app/countries
    ECHO after now Germany has been added
    curl https://basicwebemployee-i4sibuqq3a-ul.a.run.app/country
    """

    def __init__(self, file_name):
        self.folder_name = '/home/dfbrownnz/basic_web_employee/data/'  # /home/dfbrownnz/basic_web_employee/data/tasks.json
        self.file_name = file_name
        print(f" init in c_data_json {self.folder_name}{self.file_name}")
        self.task_list = []
        self.task_id_list = []

    def test(self):
        process_list = [3]
        for process in process_list:
            if process == 1:
                self.file_from_object()
                self.tasks_print()
            if process == 2:
                # function to support adding a record
                print(f"does the task id exist? {self.field_task_id_exist(self.task_id_list, task_new['task_id'])}")
                print(f"Max task id {self.field_task_id_max(self.task_id_list)}")
            if process == 3:
                # adding a record
                self.file_from_object()
                task_new = {'task_id': 5, 'person': 'Ralph', 'group': 'Cop', 'description': 'next outing meet',
                            'next_date': 20230817}
                self.tasks_add_rcd(task_new)

    def file_from_object(self):
        # print(f" this is c_data_json {self.folder_name}{self.file_name}" )
        with open(self.folder_name + self.file_name, 'r', encoding='utf-8') as f_in_obj:
            json_data = json.load(f_in_obj)
        self.json_refresh(json_data)

    def file_to_object(self, task_rcds):
        # print(f" this is c_data_json {self.folder_name}{self.file_name} and task_rcds { task_rcds}" )
        with open(self.folder_name + self.file_name, 'w', encoding='utf-8') as f_out_obj:
            json.dump(task_rcds, f_out_obj, indent=2)
        self.json_refresh(task_rcds)

    def json_refresh(self, json_data):
        self.task_list = json_data['tasks']
        self.task_id_list = self.field_task_id_return_list()

    def tasks_add_rcd(self, task_new):
        """ if the task id exists delete the record and replace it with the new record OTHERWISE just add the new record """
        # print(f" tasks_add_rcd {task_new}" )
        if self.field_task_id_exist(self.task_id_list, task_new['task_id']):

            locations = [i for i, t in enumerate(self.task_list) if t['task_id'] == task_new['task_id']]
            # [(i,) + item for i, item in enumerate(d.items(), 1)]
            # del self.task_list[locations] #= task_new

            print(f" Task ID exists {task_new['task_id']} in {locations} ")
        else:
            self.task_list.append(task_new)

        jsondata = {}
        jsondata['tasks'] = self.task_list
        self.file_to_object(jsondata)

    def tasks_print(self):
        print(f" this is tasks_print {self.folder_name}{self.file_name} ")
        for idx, val in enumerate(self.task_list):
            print(f" {idx} {val} ")

    def field_task_id_exist(self, task_id_list, task_id):
        """does the task id exist """
        if task_id in task_id_list:
            return True
        else:
            return False

    def field_task_id_max(self, task_id_list):
        """does the task id exist """
        return max(task_id_list)

    def field_task_id_return_list(self):
        """does the task id exist """
        task_id_list = []
        for idx, task_rcd in enumerate(self.task_list):
            task_id_list.append(int(task_rcd['task_id']))
        # max_val = max( list(task_rcds['task_id'].values()) )

        return task_id_list

    # def operation_update_rcd(self, todo_record_new):
    #     data = self.operation_from_file()
    #     for task_index, task_record in enumerate(data['todo']):
    #         if task_record['task_id'] == todo_record_new.task_id:
    #             # print( f"operation_update_rcd {task_index} updated  ")
    #             del data['todo'][task_index]
    #     data['todo'].append(todo_record_new.__dict__)
    #     self.operation_to_file(data)


if __name__ == '__main__':
    file_name = 'tasks.json'
    ma = cDataTask(file_name=file_name)
    ma.test()

