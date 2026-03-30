from . db_enum import DbEnum

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
            pass
        except:
            pass
    