
import random
from datetime import datetime

"""
    We declare here a functions that generate random numbers like account bank, isss number, 
    dui number among other important fields that the employee needs
"""

def generate_employee_code(number_employee):
    return f'P-{str(number_employee).zfill(5)}'

def generate_bank_account():
    return f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def generate_dui():
    return f"{random.randint(10000000, 99999999)}-{random.randint(0, 9)}"

def generate_nit():
    return f"{random.randint(0, 9999)}-{random.randint(0, 999999)}-{random.randint(0, 999)}-{random.randint(0, 9)}"

def generate_isss():
    return f"{random.randint(100000000, 999999999)}"

def generate_nup():
    return f"{random.randint(100000000000, 999999999999)}"

def generate_status():
    return random.choice(["Soltero(a)", "Casado(a)", "Divorciado(a)"])

def generate_blood():
    return random.choice(["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])

def generate_type_bank_account():
    return random.choice(["Ahorro", "Corriente"])

def generate_salary():
    return random.uniform(365, 5000)

def generate_driver_license():
    return random.choice([True, False])

def generate_phone_number():
    return f"{random.randint(6000, 7999)}-{random.randint(1000, 9999)}"

def generate_date(start_year, end_year):
    return f"{random.randint(start_year, end_year):04d}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"

def generate_employee_data():
    """
        These dates are the ones that will be parameters for the other calculations
    """
    birth_date = generate_date(1980, 1990)
    hire_date = generate_date(2009, 2023)
    """
        has_retirement is randomly chosen between True and False.
        has_dismissal is randomly chosen between True and False only if has_retirement is False, 
        If has_retirement is True, then has_dismissal is set to False.
        has_resignation is randomly chosen between True and False only if retirement_date or dismissal_date is None 
        (that is, if there is no retirement or dismissal date). If there is a retirement or termination date, 
        then has_resignation is set to False.
    """
    has_retirement = random.choice([True, False])
    has_dismissal = random.choice([True, False]) if not has_retirement else False
    has_resignation = random.choice([True, False]) if not (has_dismissal or has_retirement) else False
    state = "A" if not (has_retirement or has_dismissal or has_resignation) else "I"
    retirement_date = dismissal_date = resignation_date = None
    """
        In this part of the function we evaluate which of all the options is "True" and from that we find a random date 
        that is greater than the hiring date by at least one day
    """
    if has_retirement:
        retirement_date = generate_date(2009, 2023)
        while datetime.strptime(retirement_date, "%Y-%m-%d") <= datetime.strptime(hire_date, "%Y-%m-%d"):
            retirement_date = generate_date(2009, 2023)
    elif has_dismissal:
        dismissal_date = generate_date(2009, 2023)
        while datetime.strptime(dismissal_date, "%Y-%m-%d") <= datetime.strptime(hire_date, "%Y-%m-%d"):
            dismissal_date = generate_date(2009, 2023)
    elif has_resignation:
        resignation_date = generate_date(2009, 2023)
        while datetime.strptime(resignation_date, "%Y-%m-%d") <= datetime.strptime(hire_date, "%Y-%m-%d"):
            resignation_date = generate_date(2009, 2023)
    return {
        "birth_date": birth_date,
        "hire_date": hire_date,
        "has_retirement": has_retirement,
        "retirement_date": retirement_date,
        "has_dismissal": has_dismissal,
        "dismissal_date": dismissal_date,
        "has_resignation": has_resignation,
        "resignation_date": resignation_date,
        "state": state
    }
