
import psycopg2

"""
    Import connect configuration of database 
    Declare a cursor for you can use and execute queries in the database
    And finally confirm transaction and close connection
"""

from Data import Banks
from Connection import ConnectionDB
from Functions import Messages

def insert_bank(cursor, bank_code, bank_name, id_user_creation):
    cursor.execute(
        "INSERT INTO GT.BANK (BANK_CODE, BANK_NAME, ID_USER_CREATION) VALUES (%s, %s, %s)",
        (bank_code, bank_name, id_user_creation)
    )

try:
    connection = ConnectionDB.get_db_connection()
    cursor_connection = ConnectionDB.create_cursor(connection)
    id_user_creation = ConnectionDB.get_id_user(cursor_connection)
    for bank_name in Banks.bank:
        insert_bank(
            cursor_connection, 
            (Banks.bank.index(bank_name) + 1), 
            bank_name, id_user_creation)
    connection.commit()
    Messages.success_message()
except psycopg2.Error as e:
    Messages.error_message(e)
finally:
    if connection:
        connection.close()
