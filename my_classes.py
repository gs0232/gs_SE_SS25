from my_functions import estimate_max_hr
from datetime import datetime

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Subject(Person):

    def __init__(self, first_name, last_name, sex, dateofbirth):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__dateofbirth = datetime.strptime(dateofbirth, "%d.%m.%Y")
        self.age =  datetime.today().year- self.__dateofbirth.year

    def estimate_max_hr(self):
        self.max_hr = estimate_max_hr(self.age, self.sex)

    def __str__(self):
        return f"{self.first_name} {self.last_name} \nGender: {self.sex} \nAge: {self.__dateofbirth} \nEstimated HR: {self.max_hr}"


class Supervisor(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.postition = "supervisor"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Experiment():

    def __init__(self, experiment_name, date):
        self.experiment_name = experiment_name
        self.date = date

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return f"Experiment: {self.experiment_name} \nDatum: {self.date} \nVersuchsperson: {self.subject or 'Keine'} \nBetreuer: {self.supervisor or 'Keiner'}"