# Interface for registration system

from abc import ABC, abstractmethod


class UserRegistrationInterface(ABC):

    @abstractmethod
    def collect_personal_info(self):
        pass

    @abstractmethod
    def collect_educational_professional_details(self):
        pass

    @abstractmethod
    def collect_workshop_details(self):
        pass

    @abstractmethod
    def submit_registration(self):
        pass
