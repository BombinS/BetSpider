import logging

class ValidateMatchInfo():

    def __init__(self, matchInfo):
        self.matchInfo = matchInfo

    def process(self):
        if "match" not in self.matchInfo:                                                     # 1
            logging.error(f"Отсутсвует атрибут \"match\". {self.matchInfo}")
        if "date" not in self.matchInfo:                                                      # 2
            logging.error(f"Отсутсвует атрибут \"date\". {self.matchInfo}")
        if "datetime" not in self.matchInfo:                                                  # 3
            logging.error(f"Отсутсвует атрибут \"datetime\". {self.matchInfo}")
        if "homeScore" not in self.matchInfo:                                                 # 4
            logging.error(f"Отсутсвует атрибут \"homeScore\". {self.matchInfo}")
        if "awayScore" not in self.matchInfo:                                                 # 5
            logging.error(f"Отсутсвует атрибут \"awayScore\". {self.matchInfo}")
        if "total" not in self.matchInfo:                                                     # 6
            logging.error(f"Отсутсвует атрибут \"total\". {self.matchInfo}")
        if "1stQuarterHome" not in self.matchInfo:                                            # 7
            logging.error(f"Отсутсвует атрибут \"1stQuarterHome\". {self.matchInfo}")
        if "1stQuarterAway" not in self.matchInfo:                                            # 8
            logging.error(f"Отсутсвует атрибут \"1stQuarterAway\". {self.matchInfo}")
        if "1stQuarterTotal" not in self.matchInfo:                                           # 9
            logging.error(f"Отсутсвует атрибут \"1stQuarterTotal\". {self.matchInfo}")
        if "2ndQuarterHome" not in self.matchInfo:                                            # 10
            logging.error(f"Отсутсвует атрибут \"2ndQuarterHome\". {self.matchInfo}")
        if "2ndQuarterAway" not in self.matchInfo:                                            # 11
            logging.error(f"Отсутсвует атрибут \"2ndQuarterAway\". {self.matchInfo}")
        if "2ndQuarterTotal" not in self.matchInfo:                                           # 12
            logging.error(f"Отсутсвует атрибут \"2ndQuarterTotal\". {self.matchInfo}")
        if "3rdQuarterHome" not in self.matchInfo:                                            # 13
            logging.error(f"Отсутсвует атрибут \"3rdQuarterHome\". {self.matchInfo}")
        if "3rdQuarterAway" not in self.matchInfo:                                            # 14
            logging.error(f"Отсутсвует атрибут \"3rdQuarterAway\". {self.matchInfo}")
        if "3rdQuarterTotal" not in self.matchInfo:                                           # 15
            logging.error(f"Отсутсвует атрибут \"3rdQuarterTotal\". {self.matchInfo}")
        if "4thQuarterHome" not in self.matchInfo:                                            # 16
            logging.error(f"Отсутсвует атрибут \"4thQuarterHome\". {self.matchInfo}")
        if "4thQuarterAway" not in self.matchInfo:                                            # 17
            logging.error(f"Отсутсвует атрибут \"4thQuarterAway\". {self.matchInfo}")
        if "4thQuarterTotal" not in self.matchInfo:                                           # 18
            logging.error(f"Отсутсвует атрибут \"4thQuarterTotal\". {self.matchInfo}")
        if "oddHomeWin" not in self.matchInfo:                                                # 19
            logging.error(f"Отсутсвует атрибут \"oddHomeWin\". {self.matchInfo}")
        if "oddDraw" not in self.matchInfo:                                                   # 20
            logging.error(f"Отсутсвует атрибут \"oddDraw\". {self.matchInfo}")
        if "oddAwayWin" not in self.matchInfo:                                                # 21
            logging.error(f"Отсутсвует атрибут \"oddAwayWin\". {self.matchInfo}")
        if "1X2Margin" not in self.matchInfo:                                                 # 22
            logging.error(f"Отсутсвует атрибут \"1X2Margin\". {self.matchInfo}")
        if "oddHomeWinPercent" not in self.matchInfo:                                         # 23
            logging.error(f"Отсутсвует атрибут \"oddHomeWinPercent\". {self.matchInfo}")            
        if "oddDrawPercent" not in self.matchInfo:                                            # 24
            logging.error(f"Отсутсвует атрибут \"oddDrawPercent\". {self.matchInfo}")  
        if "oddAwayWinPercent" not in self.matchInfo:                                         # 25
            logging.error(f"Отсутсвует атрибут \"oddAwayWinPercent\". {self.matchInfo}")  
        if "thresholdTotal" not in self.matchInfo:                                            # 26
            logging.error(f"Отсутсвует атрибут \"thresholdTotal\". {self.matchInfo}")  
        if "thresholdTotalQuarter" not in self.matchInfo:                                     # 27
            logging.error(f"Отсутсвует атрибут \"thresholdTotalQuarter\". {self.matchInfo}")  
