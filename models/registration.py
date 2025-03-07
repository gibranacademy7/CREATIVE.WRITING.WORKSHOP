#  Main registration handling class:

from models.user_form import StudentFormUnder18, AdultFormOver18, ProfessionalForm
from models.payment_methods import BankTransferPayment, PayPalPayment, VisaCardPayment, InstallmentPayment
from models.registration_datetime import RegistrationDateTime

class Registration:

    def __init__(self, user_type: str, payment_method: str):
        self.user_type = user_type
        self.payment_method = payment_method
        self.form = None
        self.payment_processor = None
        self.timestamp = RegistrationDateTime.get_registration_timestamp()

    def create_registration_form(self):
        if self.user_type == 'under18':
            self.form = StudentFormUnder18()
        elif self.user_type == 'over18':
            self.form = AdultFormOver18()
        elif self.user_type == 'professional':
            self.form = ProfessionalForm()
        else:
            raise ValueError("Invalid user type.")

        self.form.collect_personal_info()
        self.form.collect_educational_professional_details()
        self.form.collect_workshop_details()

    def process_payment(self):
        if self.payment_method == 'bank':
            self.payment_processor = BankTransferPayment()
        elif self.payment_method == 'paypal':
            self.payment_processor = PayPalPayment()
        elif self.payment_method == 'visa':
            self.payment_processor = VisaCardPayment()
        elif self.payment_method == 'installment':
            self.payment_processor = InstallmentPayment()
        else:
            raise ValueError("Invalid payment method.")

        self.payment_processor.process_payment(2000.0)  # assuming a fixed payment amount for simplicity


if __name__ == "__main__":
    # Example of creating a registration for an adult participant with PayPal payment
    registration = Registration(user_type='over18', payment_method='paypal')
    registration.create_registration_form()
    registration.process_payment()
