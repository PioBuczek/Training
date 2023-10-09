# simple connect with postgresql

import psycopg2

db_connect = {
    "database": "db_connect",
    "user": "Piotrek",
    "password": "Piotrek",
    "host": "localhost",
    "port": "5432",
}

conn = psycopg2.connect(**db_connect)
cur = conn.cursor()
cur.execute(
    """
CREATE TABLE borows(
            id SERIAL PRIMARY KEY,
            name TEXT,
            book TEXT)
"""
)
conn.commit()
conn.close()
cur.close()
