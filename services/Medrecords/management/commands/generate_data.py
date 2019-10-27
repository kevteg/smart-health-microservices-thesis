from django.core.management.base import BaseCommand
from random import randint, getrandbits, choice
from faker import Faker
from Medrecords.models import Record, Patient


class Command(BaseCommand):
    help = 'Generate random but statiscally correct data for Records and Patients'

    def add_arguments(self, parser):
        parser.add_argument('patients', type=int, help='Number of patients to create')

    def create_patient(self, fake):

        notes = {
            'tipo_de_sangre': choice(['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
),
            'HCM': f'{randint(20, 40)} pg',
            'Hematocrito': f'{randint(25, 70)}%',
            'globulos_rojos': f'{randint(4, 6)} millones/ µL',
            'VCM': f'{randint(4, 6)} fL'
        }
        patient = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.date_between(start_date="-99y", end_date="today"),
            'notes': notes
        }
        patient = Patient(**patient)
        patient.save()
        return patient

    def create_record(self, fake, reasons, patient):
        toxic_habits_list = ['Tabaco', 'Cafe', 'Alcohol', 'Otras drogras']
        number_of_problems = randint(1, 4)
        number_of_toxic_habits = randint(0, len(toxic_habits_list))
        problems_summary = {}
        toxic_habits = {}
        for problem in range(number_of_problems):
            summary = fake.sentence(nb_words=30, variable_nb_words=True)
            problems_summary[choice(reasons)] = summary
        for habit in range(number_of_toxic_habits):
            summary = fake.sentence(nb_words=10, variable_nb_words=True)
            toxic_habits[choice(toxic_habits_list)] = summary

        record = {
            'reason': reasons[randint(0, len (reasons))],
            'problems_summary': problems_summary,
            'diagnostic': fake.sentence(nb_words=100, variable_nb_words=True),
            'initial_planning': fake.sentence(nb_words=100, variable_nb_words=True),
            'consult_notes': {'Importante': fake.sentence(nb_words=100, variable_nb_words=True)},
            'medical_recomendations': {'recomendacion inicial': fake.sentence(nb_words=100, variable_nb_words=True)},
            'summary': {'Resumen final': fake.sentence(nb_words=100, variable_nb_words=True)},
            'family_background': {'Herencia familiar': fake.sentence(nb_words=10, variable_nb_words=True)},
            'toxic_habits': toxic_habits,
            'patient': patient
        }
        record = Record(**record)
        record.save()

    def handle(self, *args, **kwargs):
        number_of_patients = kwargs['patients']
        fake = Faker()
        reasons = open('reasons.txt', 'r')
        reasons_list = reasons.read().split('\n')
        for patient in range(number_of_patients):
            self.stdout.write(f'Creating patient {patient}')
            #Creating from 1 to 4 records per each patient
            number_of_records = randint(1, 4)
            patient = self.create_patient(fake)
            for record in range(number_of_records):
                self.create_record(fake, reasons_list, patient)


