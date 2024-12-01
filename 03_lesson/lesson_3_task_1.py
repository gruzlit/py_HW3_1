class User:


    def __init__(self,first_name,last_name,first_name_and_last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.first_name_and_last_name = first_name_and_last_name


    def sayFN(self):
        print(self.first_name)

    def sayLN(self):
        print(self.last_name)

    def sayF_and_L(self):
        print(self.first_name_and_last_name)
