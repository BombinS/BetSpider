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

    # Маркеры тоталов
    # isTotalOverMoreThem1Points  true if total - 1  >= treshholdTotal
    # isTotalOverMoreThem3Points  true if total - 3  >= treshholdTotal
    # isTotalOverMoreThem7Points  true if total - 7  >= treshholdTotal    
    # isTotalOverMoreThem12Points true if total - 12 >= treshholdTotal    
    # isTotalLessMoreThem1Points  true if total + 1  < treshholdTotal
    # isTotalLessMoreThem3Points  true if total + 3  < treshholdTotal
    # isTotalLessMoreThem7Points  true if total + 7  < treshholdTotal    
    # isTotalLessMoreThem12Points true if total + 12 < treshholdTotal    

    def create_table_basketball_analisys_totals(self):
        with self.conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS ftBasketballAnalisysTotal 
                    (
                        id                                   SERIAL PRIMARY KEY,
                        sourceMatchId                        INT,
                        isTotalOverMoreThem1Points           BOOL,
                        isTotalOverMoreThem3Points           BOOL,
                        isTotalOverMoreThem7Points           BOOL,
                        isTotalOverMoreThem12Points          BOOL,
                        isTotalLessMoreThem1Points           BOOL,
                        isTotalLessMoreThem3Points           BOOL,
                        isTotalLessMoreThem7Points           BOOL,
                        isTotalLessMoreThem12Points          BOOL
                    )
                    """
                )
                self.conn.commit()
            except Exception as e:
                logging.error(e)
