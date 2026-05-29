
import psycopg2
def get_connection():
    conn=psycopg2.connect(
        dbname="school_db",
        user="postgres",
        password="muskan123",
        port="5432"
    )
    cursor=conn.cursor()
    return conn,cursor