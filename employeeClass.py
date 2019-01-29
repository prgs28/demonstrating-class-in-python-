class Employee:

    def __init__(self, NAME, ID, department, title):
        self.__NAME = NAME
        self.__ID = ID
        self.__department = department
        self.__title = title

    def get_name(self):
        return self.__NAME

    def get_id(self):
        return self.__ID

    def deptGet(self):
        return self.__department

    def set_NAME(self, NAME):
        self.__NAME = NAME

    def set_ID(self, ID):
        self.__ID = ID

    def dept(self, department):
        self.__department = department

    def titleSet(self, title):
        self.__title = title

    def titleGet(self):
        return self.__title

    def __str__(self):
        return 'Name: ' + self.__NAME + \
               '\nID number: ' + self.__ID + \
               '\nDepartment: ' + self.__department + \
               '\nTitle: ' + self.__title
