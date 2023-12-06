

import psycopg2

"""
    Import connect configuration of database 
    Declare a cursor for you can use and execute queries in the database
    And finally confirm transaction and close connection
"""

from Data import OrganizationUnit
from Connection import ConnectionDB
from Functions import Messages

def insert_organizational_unit(cursor, organizational_unit_code, organizational_unit_name, status, id_user_creation):
    cursor.execute(
        "INSERT INTO HR.ORGANIZATIONAL_UNIT (ORGANIZATIONAL_UNIT_CODE, ORGANIZATIONAL_UNIT_NAME, STATUS, ID_USER_CREATION) VALUES (%s, %s, %s, %s)",
        (organizational_unit_code, organizational_unit_name, status, id_user_creation)
    )

try:
    connection = ConnectionDB.get_db_connection()
    cursor_connection = ConnectionDB.create_cursor(connection)
    id_user_creation = ConnectionDB.get_id_user(cursor_connection)
    for organizational_unit_name in OrganizationUnit.Organizations:
        insert_organizational_unit(
            cursor_connection, 
            (OrganizationUnit.Organizations.index(organizational_unit_name) + 1), 
            organizational_unit_name, "A", id_user_creation)
    connection.commit()
    Messages.success_message()
except psycopg2.Error as e:
    Messages.error_message(e)
finally:
    if connection:
        connection.close()
