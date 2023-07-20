from person import Person
from enroll import Enroll

class Student(Person):

    def __init__(self, first_name, last_name, date_of_birth, phone_number, address, international = False):
        super().__init__(first_name, last_name, date_of_birth, phone_number, address)
        self.international = international
        self.enrolled = []

    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise ValueError("Invalid Enroll...")
        self.enrolled.append(enroll)

    def is_on_probation(self):
        return False
    
    def is_part_time(self):
        return len(self.enrolled) <= 3
    

