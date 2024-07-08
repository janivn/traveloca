from django.core.management.base import BaseCommand
from django.db import transaction
from fire.models import TransientHouseLocations, Owner, TransientHouse, RoomSpecifiction, Room

class Command(BaseCommand):
    help = 'Populates initial data into the database'

    def handle(self, *args, **kwargs):
        populate_data()

def populate_data():
    locations_data = [
        {
            'name': 'Beach House',
            'latitude': 9.7421,
            'longitude': 118.7397,
            'address': '123 Beachfront Road',
            'city': 'Puerto Princesa',
            'country': 'Philippines',
        },
        {
            'name': 'City Apartment',
            'latitude': 9.7422,
            'longitude': 118.7398,
            'address': '456 Downtown Avenue',
            'city': 'Puerto Princesa',
            'country': 'Philippines',
        },
        {
            'name': 'Mountain Cabin',
            'latitude': 9.7423,
            'longitude': 118.7399,
            'address': '789 Pine Tree Lane',
            'city': 'Puerto Princesa',
            'country': 'Philippines',
        }
    ]

    owners_data = [
        {
            'first_name': 'John',
            'middle_name': 'Michael',
            'last_name': 'Doe',
            'contact_information': 'john.doe@example.com',
        },
        {
            'first_name': 'Jane',
            'middle_name': 'Elizabeth',
            'last_name': 'Smith',
            'contact_information': 'jane.smith@example.com',
        },
        {
            'first_name': 'Robert',
            'middle_name': None,
            'last_name': 'Johnson',
            'contact_information': 'robert.johnson@example.com',
        }
    ]

    houses_data = [
        {
            'name': 'Seaside Retreat',
            'description': 'A cozy house by the beach',
            'price_per_night': 150.00,
            'capacity': 4,
            'location': locations_data[0],
        },
        {
            'name': 'City View Apartment',
            'description': 'Modern apartment with city skyline view',
            'price_per_night': 200.00,
            'capacity': 2,
            'location': locations_data[1],
        },
        {
            'name': 'Mountain Hideaway',
            'description': 'Rustic cabin in the mountains',
            'price_per_night': 100.00,
            'capacity': 6,
            'location': locations_data[2],
        }
    ]

    specs_data = [
        {'name': 'Double Bed'},
        {'name': 'Ocean View'},
        {'name': 'Fireplace'},
    ]

    rooms_data = [
        {
            'transient_house': houses_data[0],
            'name': 'Master Bedroom',
            'description': 'Spacious room with ocean view',
            'specification': specs_data[0],
        },
        {
            'transient_house': houses_data[1],
            'name': 'Studio Apartment',
            'description': 'Compact living space in the heart of the city',
            'specification': specs_data[1],
        },
        {
            'transient_house': houses_data[2],
            'name': 'Cozy Cabin Room',
            'description': 'Comfortable room with fireplace',
            'specification': specs_data[2],
        },
    ]

    # Populate data using transactions to ensure atomicity
    with transaction.atomic():
        for location_data in locations_data:
            # Check if the location already exists
            location, created = TransientHouseLocations.objects.get_or_create(
                name=location_data['name'],
                defaults=location_data
            )

        for owner_data in owners_data:
            Owner.objects.create(**owner_data)

        for house_data in houses_data:
            location = TransientHouseLocations.objects.get(name=house_data['location']['name'])
            house_data['location'] = location
            TransientHouse.objects.create(**house_data)

        for spec_data in specs_data:
            RoomSpecifiction.objects.create(**spec_data)

        for room_data in rooms_data:
            house = TransientHouse.objects.get(name=room_data['transient_house']['name'])
            spec = RoomSpecifiction.objects.get(name=room_data['specification']['name'])
            room_data['transient_house'] = house
            room_data['specification'] = spec
            Room.objects.create(**room_data)
