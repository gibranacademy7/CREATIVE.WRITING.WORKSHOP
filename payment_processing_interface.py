# Interface for payment processing:

from abc import ABC, abstractmethod

class PaymentProcessingInterface(ABC):

    @abstractmethod
    def process_payment(self, amount: float):
        pass
