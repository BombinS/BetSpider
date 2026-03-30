from . db_enum import DbEnum
import logging

class AnalisysTotal:

    def __init__(self, conn, type):
        self.conn = conn
        self.type = type

    def process(self):
        match self.type:
            case DbEnum.FILL_TABLE_BASKETBALL_ANALISYS_TOTALS:
                self.analisys_total_basketball()

    def analisys_total_basketball(self):
        # запрос на получение идентификторов необработанных матчей 
        # каких id из ftbasketballresults нет в качестве 'sourceMatchId' в ftbasketballanalisystotal
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT t1.id FROM ftbasketballresults as t1
                    LEFT JOIN ftbasketballanalisystotal as t2 on t1.id = t2.sourcematchid
                    WHERE T2.sourcematchid is NULL
                    """
                )
                results = cur.fetchall()
        except Exception as e:
            logging.error(f"analisys_total_basketball #1: {e}")
    