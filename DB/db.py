#!/bin/usr/env python

import psycopg2
from contextlib import closing
import logging
logging.basicConfig(filename="dd.log", filemode="w", level=logging.DEBUG, encoding="utf-8")

# подключение к Pg
def init_connection():
    conn = psycopg2.connect(
        host = "localhost",
        port = "5432",
        database="BetSpyder",
        user = "postgres",
        password = "!QAZ1qaz19770517"
    )
    return conn

# создание таблицы баскетбольной статистики
def create_table_basketball(conn):
    with conn.cursor() as cur:
        try:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS table_01
                (
                    id SERIAL PRIMARY KEY,
                    homeTeam VARCHAR(100),
                    awayTeam VARCHAR(100)
                )    
                """
            )
            conn.commit()
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    with closing(init_connection()) as conn:
        create_table_basketball(conn)