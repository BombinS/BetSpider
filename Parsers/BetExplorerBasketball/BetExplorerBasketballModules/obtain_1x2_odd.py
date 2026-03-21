class Obtain1X2Odds:

    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo
        self.xpath1X2 = "//a[@class='list-tabs__item__in current' and text()='1X2']"
        self.xpathRaw = "//tr[@class=' odd' or @class=' even']"
        self.xpathOddCell = "//td[@data-odd!='']"
        self.timeout = 5000

    def process(self):
        self.page.wait_for_selector(f"xpath={self.xpath1X2}", timeout = self.timeout)
        self.matchInfo["oddHomeWin"] = []
        self.matchInfo["oddDraw"] = []
        self.matchInfo["oddAwayWin"] = []
        rows = self.page.locator(f"xpath={self.xpathRaw}")
        for i in range(rows.count()):
            cells = rows.nth(i).locator(self.xpathOddCell)
            self.matchInfo["oddHomeWin"].append(cells.nth(0).inner_text())
            self.matchInfo["oddDraw"].append(cells.nth(1).inner_text())
            self.matchInfo["oddAwayWin"].append(cells.nth(2).inner_text())
        self.matchInfo["oddHomeWin"] = self.getAvg(self.matchInfo["oddHomeWin"])
        self.matchInfo["oddDraw"] = self.getAvg(self.matchInfo["oddDraw"])
        self.matchInfo["oddAwayWin"] = self.getAvg(self.matchInfo["oddAwayWin"])
        self.matchInfo["1X2Margin"] = round((1 - 1/(1/self.matchInfo["oddHomeWin"] + 1/self.matchInfo["oddDraw"] + 1/self.matchInfo["oddAwayWin"])) * 100, 1)
        self.matchInfo["oddHomeWinPercent"] = round((1/self.matchInfo["oddHomeWin"])/(1/self.matchInfo["oddHomeWin"] + 1/self.matchInfo["oddDraw"] + 1/self.matchInfo["oddAwayWin"]) * 100, 1)
        self.matchInfo["oddDrawPercent"] = round((1/self.matchInfo["oddDraw"])/(1/self.matchInfo["oddHomeWin"] + 1/self.matchInfo["oddDraw"] + 1/self.matchInfo["oddAwayWin"]) * 100, 1)
        self.matchInfo["oddAwayWinPercent"] = round((1/self.matchInfo["oddAwayWin"])/(1/self.matchInfo["oddHomeWin"] + 1/self.matchInfo["oddDraw"] + 1/self.matchInfo["oddAwayWin"]) * 100, 1)

    def getAvg(self, odds):
        sum = 0.0
        for i in range(len(odds)):
            sum = sum + float(odds[i])
        return round(sum/len(odds), 2)