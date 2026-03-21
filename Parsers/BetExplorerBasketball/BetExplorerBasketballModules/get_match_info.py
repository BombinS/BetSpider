import logging

from . click_match import ClickMatch
from . obtain_datetime import ObtainDatetime
from . obtain_match_results import ObtainMatchResults
from . click_1x2 import Click1X2
from . obtain_1x2_odd import Obtain1X2Odds

class GetMatchInfo:
    
    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo
        self.timeout = 5000

    def process(self):
            # перейти в конкретный матч
            xpath = f'//tr[contains(., "{self.matchInfo['match']}") and contains(., "{self.matchInfo['date']}")]//td[@class="h-text-left"]//a'
            ClickMatch(self.page, xpath).process()
            # переопределение даты матча
            ObtainDatetime(self.page, self.matchInfo).process()
            # получение результатов матча
            ObtainMatchResults(self.page, self.matchInfo).process()
            # получение коэффициентов 1X2
            Click1X2(self.page).process()
            Obtain1X2Odds(self.page, self.matchInfo).process()
            # получение коэффициентов U/O

