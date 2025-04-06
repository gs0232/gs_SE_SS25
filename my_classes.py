from my_functions import estimate_max_hr

class Subject():

    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        self.max_hr = estimate_max_hr(self.age, self.sex)

    def __str__(self):
        return f"{self.first_name} {self.last_name} \nGender: {self.sex} \nAge: {self.age} \nEstimated HR: {self.max_hr}"


class Supervisor():

    def __init__(self, supervisor):
        self.supervisor = supervisor

    def __str__(self):
        return f"{self.supervisor}"



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