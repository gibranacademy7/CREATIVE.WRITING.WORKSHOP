"""

***    Creative Writing Workshops ***

**Objective:**
Develop a comprehensive registration system for a "Creative Writing Workshops" that includes a
user-friendly interface for personal information entry and a robust financial management system for
processing online payments.
The system should be scalable, modular, and flexible to accommodate different types of participants
and payment methods.

---

**Registration System Features:**

### **Personal Information Capture:**
The registration interface should collect the following user details:

1. **General Information:**
   - Full name of the participant
   - Age of the participant
   - Full address (including town, street, house number, building number, and postal code)

2. **Additional Information Based on Age Group:**
   - **For participants under 18:**
     - Guardian's name
     - Guardian’s ID number
   - **For participants aged 17 and above:**
     - Student’s ID number (if applicable)

3. **Educational and Professional Details:**
   - School or university name (for students)
   - Workplace (for working professionals)

4. **Workshop Details:**
   - Selection of workshop level:
     - School students (under 18)
     - Amateurs (18 and above)
     - Professionals (no age limit)
   - Selection of a preferred date and time from available workshop schedules
   - Learning objectives (reasons for joining the workshop)

5. **Date & Time of Registration:**
   - A timestamp indicating when the registration was completed

---

**Payment System Integration:**
The system must support online payment processing through multiple methods, including:

- **Bank Transfers**
- **PayPal**
- **Credit/Debit Cards** (Visa, MasterCard, etc.)
- **Installment Payment Option:** Allow participants to pay workshop fees in up to four installments.

---

**Suggested Design Patterns & Approach:**

### **1. Strategy Design Pattern (for Payment Processing):**
To enable flexibility and extensibility, the **Strategy Pattern** will be used to encapsulate different
types of payment methods.
This allows new payment strategies to be added without modifying the existing code.

- **Abstract Class:** PaymentMethod
  - Defines a method process_payment()
- **Concrete Implementations:**
  - BankTransferPayment
  - PayPalPayment
  - VisaCardPayment

### **2. Abstract Factory & Factory Method Patterns (for Registration Forms):**
These patterns facilitate the creation of different types of registration forms and payment systems,
ensuring that variations in user data are handled efficiently.

- **Abstract Class:** UserForm
  - Defines common methods and properties for all registration forms
- **Concrete Implementations:**
  - StudentFormUnder18
  - AdultFormOver18
  - ProfessionalForm

Each concrete class will implement specific validation rules and data entry fields as needed.

### **3. Interface Abstract Classes (for Registration System Architecture):**
Abstract classes will define the core structure of the registration system.

- UserRegistrationInterface (interface for common registration functionalities)
- PaymentProcessingInterface (interface for handling payments efficiently)

### **4. Payment Processing Classes:**
To handle multiple payment methods efficiently, separate classes will be created:

- BankTransferPayment
- PayPalPayment
- VisaCardPayment
- InstallmentPayment

Each class will implement process_payment() according to its respective payment method.

### **5. Date & Time Management Class:**
A dedicated class RegistrationDateTime will manage and store timestamps for each registration event.
====================================================================================================
====================================================================================================

*** Directory Structure:

creative_writing_workshop/
│
├── __init__.py
├── main.py
├── interfaces/
│   ├── user_registration_interface.py
│   ├── payment_processing_interface.py
├── models/
│   ├── user_form.py
│   ├── payment_methods.py
│   ├── registration_datetime.py
│   ├── registration.py
├── strategies/
│   ├── payment_strategy.py
└── utils/
    └── date_time_utils.py
====================================================================================================
====================================================================================================

*** DIAGRAM:

                           +----------------------------+
                           |  UserRegistrationInterface  |
                           +----------------------------+
                                   ^
                                   |
                +------------------+------------------+
                |                                      |
+---------------------------+              +----------------------------+
|      UserForm (Abstract)   |              |      PaymentProcessingInterface   |
+---------------------------+              +----------------------------+
       ^                 ^                                    ^
       |                 |                                    |
+--------------+  +---------------+            +------------------+-----------------+
| StudentForm  |  |  AdultForm    |            | BankTransferPayment  PayPalPayment  |
| Under18      |  |  Over18       |            | VisaCardPayment      InstallmentPayment|
+--------------+  +---------------+            +----------------------------------------+
       |
+---------------------------+
| ProfessionalForm (Concrete)|
+---------------------------+

====================================================================================================
====================================================================================================


*** Description of the Diagram:

Description of the Diagram:
UserRegistrationInterface:

This is the parent interface for all registration forms. It defines methods for collecting personal
information, educational/professional details, and workshop preferences.
UserForm (Abstract Class):

This is an abstract class that implements the UserRegistrationInterface and holds shared methods
for registration. The specific user forms (StudentFormUnder18, AdultFormOver18, and ProfessionalForm)
inherit from this class and implement their specific data collection methods.
PaymentProcessingInterface:

This interface defines a process_payment() method, which is implemented by different payment methods.
Payment Classes:

Concrete classes like BankTransferPayment, PayPalPayment, VisaCardPayment,
and InstallmentPayment implement the PaymentProcessingInterface and define how each type
of payment is processed.

Registration Flow:

The Registration class creates a form (via the concrete form classes) and processes payment
using one of the defined payment strategies (via PaymentProcessingInterface).
=============================================================================================

*** Summary of Design Patterns Used:

1. Strategy Pattern	    Manages different payment methods.
2. Factory Method	        Creates forms based on user type.
3. Abstract Factory	    Separates the creation of registration forms and payment methods.
4. Singleton Pattern	    Ensures a single instance for timestamp management.
5. Interface Segregation	Separates interfaces for registration and payment processing.
"""
