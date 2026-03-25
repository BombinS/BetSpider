#!/bin/usr/env python

import psycopg2, json, pathlib
from pathlib import Path
from contextlib import closing
import logging
logging.basicConfig(filename="dd.log", filemode="w", level=logging.DEBUG, encoding="utf-8")

def init_connection():
    conn = psycopg2.connect(
        host = "localhost",
        port = "5432",
        database="BetSpyder",
        user = "postgres",
        password = "!QAZ1qaz19770517"
    )
    return conn

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

def load_match(season, match):
    print(season)
    print(match)
    pass

def load_matches(season):
    with open(season, "r", encoding="utf-8") as f:
        data = json.load(f)
        for match in data["schedule"]:
            load_match(data["season"], match)

if __name__ == "__main__":
    with closing(init_connection()) as conn:
        # create_table_basketball(conn)
        path = Path("ParsedData")
        season = list(path.rglob("acb-2022-2023.json"))[0]
        load_matches(season)



