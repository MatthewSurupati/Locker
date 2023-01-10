import uuid
import random


class Generate_random:
    def my_random_string_upper(self, string_length=10):
        random = str(uuid.uuid4())
        random = random.upper()
        random = random.replace("-", "")
        return random[0:string_length]

    def my_random_string_lower(self, string_length=10):
        random = str(uuid.uuid4())
        random = random.lower()
        random = random.replace("-", "")
        return random[0:string_length]

    def combine(self):
        return Gen.my_random_string_upper(2) + Gen.my_random_string_lower(3)


Gen = Generate_random()


class PIN:
    def pin_maker(self):
        PIN = ""
        pin = random.sample(range(10), 4)
        for i in pin:
            PIN += str(i)
        return PIN


P = PIN()