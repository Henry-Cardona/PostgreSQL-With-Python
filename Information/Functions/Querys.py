
import psycopg2

"""
    We declare here a functions that generate random numbers like account bank, isss number, 
    dui number among other important fields that the employee needs
"""

def get_ubication(cursor):
    cursor.execute("SELECT ID_MUNICIPALITY, ID_DEPARTMENT FROM GT.MUNICIPALITY ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

def get_bank(cursor):
    cursor.execute("SELECT ID_BANK FROM GT.BANK ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

def get_organization_unit(cursor):
    cursor.execute("SELECT ID_ORGANIZATIONAL_UNIT FROM HR.ORGANIZATIONAL_UNIT ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()

def get_organization_unit_name(cursor, id_organization_unit):
    cursor.execute(
        "SELECT ORGANIZATIONAL_UNIT_NAME FROM HR.ORGANIZATIONAL_UNIT WHERE ID_ORGANIZATIONAL_UNIT = %s",
        (id_organization_unit,)
    )
    return cursor.fetchone()

def get_department_name(cursor, id_department):
    cursor.execute(
        "SELECT DEPARTMENT_NAME FROM GT.DEPARTMENT WHERE ID_DEPARTMENT = %s",
        (id_department,)
    )
    return cursor.fetchone()

def get_municipality_name(cursor, id_municipality):
    cursor.execute(
        "SELECT MUNICIPALITY_NAME FROM GT.MUNICIPALITY WHERE ID_MUNICIPALITY = %s",
        (id_municipality,)
    )
    return cursor.fetchone()
