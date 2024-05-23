from faker import Faker

from webapp.models import VehicleData

fake = Faker()
def data_generator(num):
    for i in range(num):
        car = VehicleData.objects.create(
            vehicle_type = fake.random_element(elements=('SUV', 'Sedan', 'Hatchback', 'Coupe', 'Convertible', 'Wagon', 'Van', 'Jeep', 'Truck', 'Bus', 'Motorcycle', 'Scooter', 'Bicycle')),
            vehicle_company = fake.company(),
            vehicle_model = fake.word(),
            vehicle_plate_number = fake.license_plate(),
            vehicle_color = fake.color_name(),
            vehicle_owner = fake.name(),
            vehicle_owner_contact = fake.phone_number()
        )
        car.save()


if __name__ == '__main__':
    data_generator(10000)
    print("done")