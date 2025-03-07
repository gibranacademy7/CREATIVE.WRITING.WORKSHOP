from models.registration import Registration
from models.registration_datetime import RegistrationDateTime
from models.user_form import StudentFormUnder18, AdultFormOver18, ProfessionalForm
from models.payment_methods import BankTransferPayment, PayPalPayment, VisaCardPayment, InstallmentPayment
from strategies.payment_strategy import PaymentStrategy


def collect_personal_info(user_type):
    """Function to collect personal information from the user"""
    personal_info = {}

    # Collecting general information
    personal_info['name'] = input("Enter your full name: ")
    personal_info['age'] = int(input("Enter your age: "))

    if user_type == 'under18':
        personal_info['guardian_name'] = input("Enter your guardian's name: ")
        personal_info['guardian_id'] = input("Enter your guardian's ID number: ")
    elif user_type == 'over18':
        personal_info['student_id'] = input("Enter your student ID number (if applicable): ")

    return personal_info


def collect_educational_professional_info(user_type):
    """Function to collect educational/professional details from the user"""
    educational_info = {}

    if user_type == 'under18':
        educational_info['school'] = input("Enter your school name: ")
    elif user_type == 'over18':
        educational_info['university'] = input("Enter your university name: ")
    else:
        educational_info['workplace'] = input("Enter your workplace: ")

    return educational_info


def collect_workshop_details():
    """Function to collect workshop details"""
    workshop_info = {}

    print("\nSelect workshop level:")
    print("1. School Students (under 18)")
    print("2. Amateurs (18 and above)")
    print("3. Professionals (no age limit)")
    workshop_level = input("Enter the level (1/2/3): ")

    if workshop_level == '1':
        workshop_info['level'] = 'School Students'
    elif workshop_level == '2':
        workshop_info['level'] = 'Amateurs'
    else:
        workshop_info['level'] = 'Professional'

    workshop_info['preferred_date'] = input("Enter your preferred workshop date (YYYY-MM-DD): ")

    return workshop_info


def collect_payment_info():
    """Function to collect payment information from the user"""
    print("\nSelect payment method:")
    print("1. Bank Transfer")
    print("2. PayPal")
    print("3. Visa Card")
    print("4. Installment (up to 4 payments)")

    payment_method = input("Enter the payment method (1/2/3/4): ")

    if payment_method == '1':
        return 'bank'
    elif payment_method == '2':
        return 'paypal'
    elif payment_method == '3':
        return 'visa'
    elif payment_method == '4':
        return 'installment'
    else:
        print("Invalid selection, defaulting to Bank Transfer.")
        return 'bank'


def main():
    # Collecting user type and handling form accordingly
    user_type = input("Enter user type (under18/over18/professional): ").strip().lower()

    # Collecting all the information from the user
    personal_info = collect_personal_info(user_type)
    educational_info = collect_educational_professional_info(user_type)
    workshop_info = collect_workshop_details()
    payment_method = collect_payment_info()

    # Create the corresponding registration form
    if user_type == 'under18':
        user_form = StudentFormUnder18()
    elif user_type == 'over18':
        user_form = AdultFormOver18()
    else:
        user_form = ProfessionalForm()

    # Assign collected info to the form
    user_form.personal_info = personal_info
    user_form.educational_info = educational_info
    user_form.workshop_info = workshop_info

    # Registration and payment processing
    registration = Registration(user_type=user_type, payment_method=payment_method)
    registration.create_registration_form()
    registration.process_payment()

    # Output registration timestamp
    print(f"\nRegistration completed at: {registration.timestamp}")
    print(f"Registration Info: {user_form.personal_info}, {user_form.educational_info}, {user_form.workshop_info}")


if __name__ == "__main__":
    main()
