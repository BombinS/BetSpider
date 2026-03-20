import logging

from . click_match import ClickMatch
from . obtain_datetime import ObtainDatetime
from . obtain_match_results import ObtainMatchResults

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

            # получение коэффициентов U/O

