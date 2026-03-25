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
                CREATE TABLE IF NOT EXISTS ftBasketballResults
                (
                    id                      SERIAL         PRIMARY KEY,
                    season                  VARCHAR(30),
                    datetime                TIMESTAMP,
                    homeTeam                VARCHAR(100),
                    awayTeam                VARCHAR(100),
                    homeScore               SMALLINT,
                    awayScore               SMALLINT,
                    total                   SMALLINT,
                    Quarter1stHome          SMALLINT,
                    Quarter1stAway          SMALLINT,
                    Quarter1stTotal         SMALLINT,                                                            
                    Quarter2ndHome          SMALLINT,
                    Quarter2ndAway          SMALLINT,
                    Quarter2ndTotal         SMALLINT,                                                            
                    Quarter3rdHome          SMALLINT,
                    Quarter3rdAway          SMALLINT,
                    Quarter3rdTotal         SMALLINT,                                                            
                    Quarter4thHome          SMALLINT,
                    Quarter4thAway          SMALLINT,
                    Quarter4thTotal         SMALLINT,
                    oddHomeWin              REAL,
                    oddDraw                 REAL,
                    oddAwayWin              REAL,
                    Margin1X2               REAL,
                    oddHomeWinPercent       REAL,
                    oddDrawPercent          REAL,
                    oddAwayWinPercent       REAL,
                    thresholdTotal          SMALLINT,
                    thresholdTotalQuarter   real             
                )    
                """
            )
            conn.commit()
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    with closing(init_connection()) as conn:
        create_table_basketball(conn)

    # "oddHomeWinPercent": 83.0,
    # "oddDrawPercent": 4.4,
    # "oddAwayWinPercent": 12.6,
    # "thresholdTotal": "167",
    # "thresholdTotalQuarter": 41.8


