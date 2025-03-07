# Concrete classes for registration forms:


from interfaces.user_registration_interface import UserRegistrationInterface
from abc import ABC, abstractmethod


class UserForm(UserRegistrationInterface, ABC):

    def __init__(self):
        self.personal_info = {}
        self.educational_info = {}
        self.workshop_info = {}

    @abstractmethod
    def collect_personal_info(self):
        pass

    @abstractmethod
    def collect_educational_professional_details(self):
        pass

    @abstractmethod
    def collect_workshop_details(self):
        pass

    def submit_registration(self):
        print(f"Registration submitted with: {self.personal_info}, {self.educational_info}, {self.workshop_info}")
        return True


class StudentFormUnder18(UserForm):

    def collect_personal_info(self):
        self.personal_info = {'name': 'John Doe', 'age': 16, 'guardian_name': 'Jane Doe', 'guardian_id': '123456'}

    def collect_educational_professional_details(self):
        self.educational_info = {'school': 'ABC High School'}

    def collect_workshop_details(self):
        self.workshop_info = {'level': 'School Students', 'preferred_date': '2025-06-01'}


class AdultFormOver18(UserForm):

    def collect_personal_info(self):
        self.personal_info = {'name': 'Alex Smith', 'age': 25, 'student_id': '987654'}

    def collect_educational_professional_details(self):
        self.educational_info = {'university': 'XYZ University'}

    def collect_workshop_details(self):
        self.workshop_info = {'level': 'Amateurs', 'preferred_date': '2025-06-01'}


class ProfessionalForm(UserForm):

    def collect_personal_info(self):
        self.personal_info = {'name': 'Alice Brown', 'age': 30}

    def collect_educational_professional_details(self):
        self.educational_info = {'workplace': 'TechCorp'}

    def collect_workshop_details(self):
        self.workshop_info = {'level': 'Professional', 'preferred_date': '2025-06-01'}
