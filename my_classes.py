from my_functions import estimate_max_hr

class Subject():

    def __init__(self, first_name, last_name, sex, age):
        self.fist_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        self.max_hr = estimate_max_hr(self.age, self.sex)
