import random
import string


class Robot:
    _used_names = set()
    
    def __init__(self):
        self.name = None
        self.reset()

    def reset(self):
        new_name = self._generate_name()

        while new_name in Robot._used_names:
            new_name = self._generate_name()

        if self.name:
            Robot._used_names.remove(self.name)

        self.name = new_name
        Robot._used_names.add(new_name)

    def _generate_name(self):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        digits = ''.join(random.choices(string.digits, k=3))
        return letters + digits

    def __del__(self):
        if hasattr(self, 'name') and self.name in Robot._used_names:
            Robot._used_names.remove(self.name)
