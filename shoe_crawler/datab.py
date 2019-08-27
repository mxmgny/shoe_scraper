import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


db_name = 'nike_database'

try:
    connection = psycopg2.connect(
        user='postgres',
        password='MaximiliaN98ujlf',
        host='127.0.0.1',
        port='5432',
        database='shoes_db'
        )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    cursor.execute("""create table Nikes(Title VARCHAR(50), Subtitle VARCHAR(50),Current_price INT )""")
    cursor.execute("""INSERT INTO Nikes VALUES('nike air max', 'men shoes', 125)""")

    connection.commit()
    print(cursor)

except psycopg2.DatabaseError as error:
    if connection:
        connection.rollback()
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
