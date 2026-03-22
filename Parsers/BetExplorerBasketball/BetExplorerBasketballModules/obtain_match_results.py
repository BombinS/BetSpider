import logging

class ObtainMatchResults:
    
    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo
        self.totalxPath = "//p[@id='js-score' and text() != '']"
        self.partialxPath = "//div[@id='js-partial' and text() != '']"
        self.timeout = 5000

    def process(self):
            try:
                # Общий результат
                self.page.wait_for_selector(f"xpath={self.totalxPath}", timeout=5000)
                totalResult = self.page.locator(f"xpath={self.totalxPath}").text_content()
                logging.info(f"Успешное получение результата матча {totalResult}")
                totalResult = totalResult.split(":")
                self.matchInfo["homeScore"] = totalResult[0].strip()
                self.matchInfo["awayScore"] = totalResult[1].strip()
                self.matchInfo["total"] = int(self.matchInfo["homeScore"]) + int(self.matchInfo["awayScore"])

                # результат таймов, периодов, четвертей
                self.page.wait_for_selector(f"xpath={self.partialxPath}", timeout=5000)
                partialResult = self.page.locator(f"xpath={self.partialxPath}").text_content()
                logging.info(f"Успешное получение результатов частей матча {partialResult}")
                partialResults = partialResult.replace("(","").replace(")","").split(",")
                partialResultClean  = []
                for x in partialResults:
                    xx = (x.strip().split(":"))
                    for y in xx:
                         partialResultClean.append(y)
                # баскетбол
                if len(partialResultClean) == 8: 
                     self.matchInfo["1stQuarterHome"] = partialResultClean[0]
                     self.matchInfo["1stQuarterAway"] = partialResultClean[1]
                     self.matchInfo["1stQuarterTotal"] = int(self.matchInfo["1stQuarterHome"]) + int(self.matchInfo["1stQuarterAway"])
                     self.matchInfo["2ndQuarterHome"] = partialResultClean[2]
                     self.matchInfo["2ndQuarterAway"] = partialResultClean[3]
                     self.matchInfo["2ndQuarterTotal"] = int(self.matchInfo["2ndQuarterHome"]) + int(self.matchInfo["2ndQuarterAway"])
                     self.matchInfo["3rdQuarterHome"] = partialResultClean[4]
                     self.matchInfo["3rdQuarterAway"] = partialResultClean[5]
                     self.matchInfo["3rdQuarterTotal"] = int(self.matchInfo["3rdQuarterHome"]) + int(self.matchInfo["3rdQuarterAway"])
                     self.matchInfo["4thQuarterHome"] = partialResultClean[6]
                     self.matchInfo["4thQuarterAway"] = partialResultClean[7]
                     self.matchInfo["4thQuarterTotal"] = int(self.matchInfo["4thQuarterHome"]) + int(self.matchInfo["4thQuarterAway"])

            except Exception as e:
                logging.error(e)
                raise 