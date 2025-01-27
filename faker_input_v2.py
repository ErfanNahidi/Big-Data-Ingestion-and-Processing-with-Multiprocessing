'''from faker import Faker
from random import randint

class StreamFastGenerator:
    def __init__(self, locale='fa_IR'):
        self.faker = Faker(locale)
    
    def generate_data(self):
        while True:
            yield {
                'first_name': self.faker.first_name(),
                'last_name': self.faker.last_name(),
                'age': randint(18, 100),
                'state': self.faker.state(),
                'city': self.faker.city(),
                'street': self.faker.street_name(),
                'building_number': self.faker.building_number(),
                'phone_number': self.faker.phone_number(),
                'post_code': self.faker.postcode()
            }'''


from faker import Faker
from random import randint

class StreamFastGenerator:
    def __init__(self, locale='fa_IR'):
        self.faker = Faker(locale)
    
    def generate_data(self, num_records):
        """Generate a batch of fake data based on the number of records requested."""
        data = []
        for _ in range(num_records):
            data.append({
                'first_name': self.faker.first_name(),
                'last_name': self.faker.last_name(),
                'age': randint(18, 100),
                'state': self.faker.state(),
                'city': self.faker.city(),
                'street': self.faker.street_name(),
                'building_number': self.faker.building_number(),
                'phone_number': self.faker.phone_number(),
                'post_code': self.faker.postcode()
            })
        return data
