from django.core.management.base import BaseCommand
from random import randint, getrandbits, choice
from faker import Faker
from Metadata.models import Doctor, Center, Ambulance


class Command(BaseCommand):
    help = 'Generate random data for Doctors, Centers and Ambulances'

    def add_arguments(self, parser):
        parser.add_argument('patients', type=int, help='Number of patients to create')

    def create_doctor(self, fake):
        doctor = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'specialty': fake.sentence(nb_words=3),
        }
        doctor = Doctor(**doctor)
        doctor.save()

    def create_ambulance(self, fake):
        location = fake.local_latlng(country_code="VE", coords_only=True)
        ambulance = {
            'location': location,
        }
        ambulance = Ambulance(**ambulance)
        ambulance.save()

    def create_center(self, fake):
        location = fake.local_latlng(country_code="VE", coords_only=True)
        center = {
            'name': fake.sentence(nb_words=3),
            'location': location,
        }
        center = Center(**center)
        center.save()

    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_centers = randint(1, 10)
        number_of_doctors = randint(100, 300)
        number_of_ambulances = randint(50, 100)
        for doctor in range(number_of_doctors):
            self.stdout.write(f'Creating doctor')
            self.create_doctor(fake)

        for center in range(number_of_centers):
            self.stdout.write(f'Creating center')
            self.create_center(fake)

        for ambulance in range(number_of_ambulances):
            self.stdout.write(f'Creating ambulance')
            self.create_ambulance(fake)

