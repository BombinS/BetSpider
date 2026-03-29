import logging
from . db_enum import DbEnum

class CreateTable():

    def __init__(self, conn, type):
        self.conn = conn
        self.type = type

    def process(self):
        match self.type:
            case DbEnum.CREATE_TABLE_BASKETBALL_RESULTS:
                self.create_table_basketball_results()
            case DbEnum.CREATE_TABLE_BASKETBALL_ANALISYS_TOTALS:
                self.create_table_basketball_analisys_totals()
        
    def create_table_basketball_results(self):
        with self.conn.cursor() as cur:
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
                        thresholdTotal          REAL,
                        thresholdTotalQuarter   REAL             
                    )    
                    """
                )
                self.conn.commit()
            except Exception as e:
                logging.error(e)

    def create_table_basketball_analisys_totals(self):
        with self.conn.cursor() as cur:
            try:
                pass
            except Exception as e:
                logging.error("e")
