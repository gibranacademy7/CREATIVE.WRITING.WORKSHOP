# Payment Strategy Pattern:

from models.payment_methods import BankTransferPayment, PayPalPayment, VisaCardPayment, InstallmentPayment

class PaymentStrategy:

    @staticmethod
    def get_payment_processor(payment_method: str):
        if payment_method == 'bank':
            return BankTransferPayment()
        elif payment_method == 'paypal':
            return PayPalPayment()
        elif payment_method == 'visa':
            return VisaCardPayment()
        elif payment_method == 'installment':
            return InstallmentPayment()
        else:
            raise ValueError("Invalid payment method.")
