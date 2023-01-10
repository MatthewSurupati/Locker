import uuid
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from kink import inject, di


class Generator:
    def generate(self):
        pass

@inject
class RandomIdGeerator(Generator):
    def generate(self):
        id_ = str("".join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(5)))
        return id_

@inject
class RandomPasswordGenerator(Generator):
    def generate(self):
        password = "".join(choice(digits) for i in range(4))
        return password