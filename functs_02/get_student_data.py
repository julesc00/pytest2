import json
import os


class StudentDB:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file, "r") as json_f:
            self.__data = json.load(json_f)

    def get_data(self, name):
        for student in self.__data["students"]:
            if student["name"] == name:
                return student

    def close(self):
        pass
