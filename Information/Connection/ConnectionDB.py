
import psycopg2

def get_db_connection():
    return psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )

def create_cursor(connection):
    return connection.cursor()

def get_id_user(cursor):
    cursor.execute("SELECT ID_USER FROM GT.USERS LIMIT 1")
    return cursor.fetchone()