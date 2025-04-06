from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    supervisor = Supervisor("Julian Huber")
    subject = Subject("Pia", "Schratt", "female", 30)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)