
import random
import psycopg2
from psycopg2 import sql

"""
    We declare here, every variables that import from another files.
    We do this to we have a better organization in the structure that create our json.
    So in the future we will always add the new imports here.
    The folder where to save new arrays for extract random information it's called 'Data'
"""

from Connection import ConnectionDB
from Data import ExtensionsEmails, FirstNames, LastNames, OrganizationUnit, Directions
from Functions import Generate, Messages, Querys

try:
    connection = ConnectionDB.get_db_connection()
    cursor_connection = ConnectionDB.create_cursor(connection)
    for employee_number in range(1, 501):
        """
            Here we have recovered all the information from the database and the random data in the arrays 
            of the Data folder, this to create as many employees as we need.
        """
        random_names, random_genre = FirstNames.random_first_name()
        random_municipality, random_department = Querys.get_ubication(cursor_connection)
        random_dates = Generate.generate_employee_data()
        random_monthly_salary = Generate.generate_salary()
        random_organization_unit = Querys.get_organization_unit(cursor_connection)
        random_job = OrganizationUnit.get_random_job(Querys.get_organization_unit_name(cursor_connection, random_organization_unit)[0])
        user_creation = ConnectionDB.get_id_user(cursor_connection)
        employee = {
            "EMPLOYEE_CODE": Generate.generate_employee_code(employee_number),
            "FIRST_NAME": ' '.join(random_names),
            "LAST_NAME": ' '.join(LastNames.random_last_name()),
            "STATUS": random_dates["state"],
            "GENDER": random_genre,
            "BIRTH_DATE": random_dates["birth_date"],
            "CIVIL_STATUS": Generate.generate_status(),
            "ADDRESS": (
                f"{Directions.random_address()}, "
                f"{Querys.get_municipality_name(cursor_connection, random_municipality)[0]}, "
                f"{Querys.get_department_name(cursor_connection, random_department)[0]}, "
                "El Salvador"
            ),
            "PHONE": Generate.generate_phone_number(),
            "CELLPHONE": Generate.generate_phone_number(),
            "BLOOD_TYPE": Generate.generate_blood(),
            "EMAIL": f"{(''.join(random_names)).lower()}{ExtensionsEmails.random_emails()}",
            "BANK": Querys.get_bank(cursor_connection),
            "ACCOUNT_BANK": Generate.generate_bank_account(),
            "ACCOUNT_TYPE": Generate.generate_type_bank_account(),
            "DRIVER_LICENSE": Generate.generate_driver_license(),
            "DUI": Generate.generate_dui(),
            "NIT": Generate.generate_nit(),
            "ISSS": Generate.generate_isss(),
            "NUP": Generate.generate_nup(),
            "DEPARTMENT": random_department,
            "MUNICIPALITY": random_municipality,
            "POSITION": random_job,
            "ADMISSION_DATE": random_dates["hire_date"],
            "RETIREMENT": random_dates["has_retirement"],
            "RETIREMENT_DATE": random_dates["retirement_date"],
            "DISMISSAL": random_dates["has_dismissal"],
            "DISMISSAL_DATE": random_dates["dismissal_date"],
            "RESIGNATION": random_dates["has_resignation"],
            "RESIGNATION_DATE": random_dates["resignation_date"],
            "MONTHLY_SALARY": round(random_monthly_salary, 2),
            "DAILY_SALARY": round(random_monthly_salary / 22, 2),
            "HOUR_WAGE": round(random_monthly_salary / 22 / 8, 2),
            "CONTRACT_DATE": random_dates["hire_date"],
            "ORGANIZATIONAL_UNIT": random_organization_unit,
            "ID_USER_CREATION": user_creation
        }
        insert_query = """
            INSERT INTO HR.EMPLOYEES
            (
                EMPLOYEE_CODE, 
                FIRST_NAME, 
                LAST_NAME, 
                STATUS, 
                GENDER, 
                BIRTH_DATE, 
                CIVIL_STATUS, 
                ADDRESS, 
                PHONE, 
                CELLPHONE,
                BLOOD_TYPE, 
                EMAIL, 
                ID_BANK, 
                ACCOUNT_BANK, 
                ACCOUNT_TYPE, 
                DRIVER_LICENSE, 
                DUI, 
                NIT, 
                ISSS, 
                NUP, 
                ID_DEPARTMENT,
                ID_MUNICIPALITY, 
                POSITION, 
                ADMISSION_DATE, 
                RETIREMENT, 
                RETIREMENT_DATE, 
                DISMISSAL, 
                DISMISSAL_DATE, 
                RESIGNATION,
                RESIGNATION_DATE, 
                MONTHLY_SALARY, 
                DAILY_SALARY, 
                HOUR_WAGE, 
                CONTRACT_DATE, 
                ID_ORGANIZATIONAL_UNIT, 
                ID_USER_CREATION
            )
            VALUES
            (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s
            )
        """
        """
            cursor_connection.execute(insert_query, ...): This line executes a SQL query using a cursor on a 
            database connection. The insert_query parameter must contain a string with the insert SQL statement.
            (...) is a tuple containing the values to be inserted into the database. Each value corresponds to 
            a field in the database table and is extracted from the employee dictionary.
            The values are ordered according to the order of the fields in the table.
        """
        cursor_connection.execute(insert_query, (
            employee["EMPLOYEE_CODE"], 
            employee["FIRST_NAME"], 
            employee["LAST_NAME"], 
            employee["STATUS"],
            employee["GENDER"], 
            employee["BIRTH_DATE"], 
            employee["CIVIL_STATUS"], 
            employee["ADDRESS"], 
            employee["PHONE"],
            employee["CELLPHONE"], 
            employee["BLOOD_TYPE"], 
            employee["EMAIL"], 
            employee["BANK"], 
            employee["ACCOUNT_BANK"],
            employee["ACCOUNT_TYPE"], 
            employee["DRIVER_LICENSE"], 
            employee["DUI"], 
            employee["NIT"], 
            employee["ISSS"], 
            employee["NUP"], 
            employee["DEPARTMENT"], 
            employee["MUNICIPALITY"], 
            employee["POSITION"], 
            employee["ADMISSION_DATE"],
            employee["RETIREMENT"], 
            employee["RETIREMENT_DATE"], 
            employee["DISMISSAL"], 
            employee["DISMISSAL_DATE"],
            employee["RESIGNATION"], 
            employee["RESIGNATION_DATE"], 
            employee["MONTHLY_SALARY"], 
            employee["DAILY_SALARY"],
            employee["HOUR_WAGE"], 
            employee["CONTRACT_DATE"], 
            employee["ORGANIZATIONAL_UNIT"], 
            employee["ID_USER_CREATION"]
        ))
    connection.commit()
    Messages.success_message()
except psycopg2.Error as e:
    Messages.error_message(e)
finally:
    if connection:
        connection.close()
