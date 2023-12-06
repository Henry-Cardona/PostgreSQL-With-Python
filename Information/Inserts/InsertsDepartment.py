
import psycopg2

"""
    Import connect configuration of database 
    Declare a cursor for you can use and execute queries in the database
    And finally confirm transaction and close connection
"""

from Data import Departments
from Connection import ConnectionDB
from Functions import Messages

def get_max_municipality_code(cursor):
    cursor.execute("SELECT COALESCE(MAX(MUNICIPALITY_CODE), 0) FROM GT.MUNICIPALITY")
    return cursor.fetchone()[0]

def insert_department(cursor, department_code, department_name, id_user_creation):
    cursor.execute(
        "INSERT INTO GT.DEPARTMENT (DEPARTMENT_CODE, DEPARTMENT_NAME, ID_USER_CREATION) VALUES (%s, %s, %s) RETURNING ID_DEPARTMENT",
        (department_code, department_name, id_user_creation)
    )
    return cursor.fetchone()[0]

def insert_municipality(cursor, municipalities, id_department, id_user_creation):
    for municipality_name in municipalities:
        cursor.execute(
            "INSERT INTO GT.MUNICIPALITY (MUNICIPALITY_CODE, MUNICIPALITY_NAME, ID_DEPARTMENT, ID_USER_CREATION) VALUES (%s, %s, %s, %s)", 
            ((get_max_municipality_code(cursor) + 1), municipality_name, id_department, id_user_creation)
        )

try:
    connection = ConnectionDB.get_db_connection()
    cursor_connection = ConnectionDB.create_cursor(connection)
    id_user_creation = ConnectionDB.get_id_user(cursor_connection)
    for department_name in Departments.department:
        id_department = insert_department(
            cursor_connection, 
            (Departments.department.index(department_name) + 1), 
            department_name, id_user_creation)
        insert_municipality(
            cursor_connection, 
            (Departments.municipality.get(department_name, [])), 
            id_department, id_user_creation)
    connection.commit()
    Messages.success_message()
except psycopg2.Error as e:
    Messages.error_message(e)
finally:
    if connection:
        connection.close()
