from faker import Faker
from django.core.management.base import BaseCommand
from webapp.models import VehicleData



class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Define the number of fake entries you want to create
        num_entries = 1000000

        for _ in range(num_entries):
            # Generate fake data
            vehicle_data = VehicleData(
                vehicle_type = fake.word(),
                vehicle_company = fake.company(),
                vehicle_model = fake.word(),
                vehicle_plate_number = fake.license_plate(),
                vehicle_color = fake.color_name(),
                vehicle_owner = fake.name(),
                vehicle_owner_contact = fake.phone_number()
            )
            
            vehicle_data.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully populated database with {num_entries} fake entries.'))



    print("done")