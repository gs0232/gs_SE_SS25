from my_functions import build_person, build_experiment, estimate_max_hr

if __name__ == "__main__":
    first_name = "Sophia"
    last_name = "Gwiggner"
    sex = "female"
    age_years = 20
    age = age_years
    experiment_name = "sakai_3_max_hr"
    date = "23.03.2025"
    supervisor = "Julian Huber"
    subject = "Aufgabe 3"

    first_person = build_person(first_name, last_name, sex, age)
    print(first_person)

    first_experiment = build_experiment(experiment_name, date, supervisor, subject)
    print(first_experiment)

    estimated_hr = estimate_max_hr(age_years, sex)
    print(estimated_hr)