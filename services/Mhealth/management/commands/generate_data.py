from django.core.management.base import BaseCommand
from random import randint, getrandbits, choice
from faker import Faker
from Mhealth.models import SmartPhoneMeta, Patient


class Command(BaseCommand):
    help = 'Generate random data correct data for Records and Patients'

    def add_arguments(self, parser):
        parser.add_argument('patients', type=int, help='Number of patients to create')

    def create_patient(self, fake):
        patient = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birth_date': fake.date_between(start_date="-99y", end_date="today"),
        }
        patient = Patient(**patient)
        patient.save()
        return patient

    def create_meta(self, fake, patient):
        location = fake.local_latlng(country_code="VE", coords_only=True)
        meta = {
            'location': location,
            'patient': patient
        }
        meta = SmartPhoneMeta(**meta)
        meta.save()

    def handle(self, *args, **kwargs):
        number_of_patients = kwargs['patients']
        fake = Faker()
        for patient in range(number_of_patients):
            self.stdout.write(f'Creating patient {patient}')
            #Creating from 1 to 4 meta data for fake phone
            number_of_metadata = randint(1, 4)
            patient = self.create_patient(fake)
            for _ in range(number_of_metadata):
                self.create_meta(fake, patient)

