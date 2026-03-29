#!/bin/usr/env python

import psycopg2, json, pathlib
from pathlib import Path
from contextlib import closing
import logging
logging.basicConfig(filename="dd.log", filemode="w", level=logging.DEBUG, encoding="utf-8")

from DbModules.db_enum import DbEnum
from DbModules.create_table import CreateTable

def init_connection():
    conn = psycopg2.connect(
        host = "localhost",
        port = "5432",
        database="BetSpyder",
        user = "postgres",
        password = "!QAZ1qaz19770517"
    )
    return conn

# def create_table_basketball(conn):
#     with conn.cursor() as cur:
#         try:
#             cur.execute(
#                 """
#                 CREATE TABLE IF NOT EXISTS ftBasketballResults
#                 (
#                     id                      SERIAL         PRIMARY KEY,
#                     season                  VARCHAR(30),
#                     datetime                TIMESTAMP,
#                     homeTeam                VARCHAR(100),
#                     awayTeam                VARCHAR(100),
#                     homeScore               SMALLINT,
#                     awayScore               SMALLINT,
#                     total                   SMALLINT,
#                     Quarter1stHome          SMALLINT,
#                     Quarter1stAway          SMALLINT,
#                     Quarter1stTotal         SMALLINT,                                                            
#                     Quarter2ndHome          SMALLINT,
#                     Quarter2ndAway          SMALLINT,
#                     Quarter2ndTotal         SMALLINT,                                                            
#                     Quarter3rdHome          SMALLINT,
#                     Quarter3rdAway          SMALLINT,
#                     Quarter3rdTotal         SMALLINT,                                                            
#                     Quarter4thHome          SMALLINT,
#                     Quarter4thAway          SMALLINT,
#                     Quarter4thTotal         SMALLINT,
#                     oddHomeWin              REAL,
#                     oddDraw                 REAL,
#                     oddAwayWin              REAL,
#                     Margin1X2               REAL,
#                     oddHomeWinPercent       REAL,
#                     oddDrawPercent          REAL,
#                     oddAwayWinPercent       REAL,
#                     thresholdTotal          REAL,
#                     thresholdTotalQuarter   REAL             
#                 )    
#                 """
#             )
#             conn.commit()
#         except Exception as e:
#             logging.error(e)

def clear_table_basketball(conn):
    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM public.ftbasketballresults")
            conn.commit()
        except Exception as e:
            logging.error(e)

def load_match(conn, season, match):
    with conn.cursor() as cur:
        try:
            parts = match["datetime"].split("-")
            normalizedDateTime = f"{parts[0].strip()} {parts[1].strip()}"
            parts = match["match"].split("-")
            normalizedHomeTeam = parts[0].strip()
            normalizedAwayTeam = parts[1].strip() 
            cur.execute(
                """
                INSERT INTO ftBasketballResults 
                (
                    season,
                    datetime,
                    homeTeam,
                    awayTeam,
                    homeScore,
                    awayScore,
                    total,
                    Quarter1stHome,
                    Quarter1stAway,
                    Quarter1stTotal,                                                            
                    Quarter2ndHome,
                    Quarter2ndAway,
                    Quarter2ndTotal,                                                            
                    Quarter3rdHome,
                    Quarter3rdAway,
                    Quarter3rdTotal,                                                            
                    Quarter4thHome,
                    Quarter4thAway,
                    Quarter4thTotal,
                    oddHomeWin,
                    oddDraw,
                    oddAwayWin,
                    Margin1X2 ,
                    oddHomeWinPercent,
                    oddDrawPercent,
                    oddAwayWinPercent,
                    thresholdTotal,
                    thresholdTotalQuarter 
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,                                                            
                    %s,
                    %s,
                    %s,                                                            
                    %s,
                    %s,
                    %s,                                                            
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s ,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    season,
                    normalizedDateTime,
                    normalizedHomeTeam,
                    normalizedAwayTeam,
                    match["homeScore"],
                    match["awayScore"],
                    match["total"],
                    match["1stQuarterHome"],
                    match["1stQuarterAway"],
                    match["1stQuarterTotal"],
                    match["2ndQuarterHome"],
                    match["2ndQuarterAway"],
                    match["2ndQuarterTotal"],
                    match["3rdQuarterHome"],
                    match["3rdQuarterAway"],
                    match["3rdQuarterTotal"],
                    match["4thQuarterHome"],
                    match["4thQuarterAway"],
                    match["4thQuarterTotal"],
                    match["oddHomeWin"],
                    match["oddDraw"],
                    match["oddAwayWin"],
                    match["1X2Margin"],
                    match["oddHomeWinPercent"],
                    match["oddDrawPercent"],
                    match["oddAwayWinPercent"],
                    match["thresholdTotal"],
                    match["thresholdTotalQuarter"]
                )
            )
            conn.commit()
        except Exception as e:
            logging.error(f"ошибка вставки матча с исключением: {e}. Матч: {match}")

def load_matches(conn, season):
    with open(season, "r", encoding="utf-8") as f:
        data = json.load(f)
        #load_match(conn, data["season"], data["schedule"][0])
        for match in data["schedule"]:
            load_match(conn, data["season"], match)

if __name__ == "__main__":

    with closing(init_connection()) as conn:
        CreateTable(conn, DbEnum.CREATE_TABLE_BASKETBALL_ANALISYS_TOTALS).process()
        exit()
        
        # create_table_basketball(conn)
        # clear_table_basketball(conn)
        path = Path("ParsedData\\Basketball")
        seasons = list(path.rglob("*.json"))
        for season in seasons:
            # считаем признаком архивного сезона длину имени спарсенного json. Если больше 8-ми (xxx.json) то архив
            if len(season.name) > 8:
                logging.info(f"Загрузка сезона {season.name}")
                load_matches(conn, season)
        
        
        
