import logging

from . click_match import ClickMatch

class GetMatchInfo:
    
    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo
        self.timeout = 5000

    def process(self):
            # перейти в конкретный матч
            xpath = f'//tr[contains(., "{self.matchInfo['match']}") and contains(., "{self.matchInfo['date']}")]//td[@class="h-text-left"]//a'
            ClickMatch(self.page, xpath).process()
            # переопределяем дату матча
            xpath_selector = "//p[@id='match-date' and text() != '']"
            self.page.wait_for_selector(f"xpath={xpath_selector}", timeout=5000)
            self.matchInfo['datetime'] = self.page.locator(f"xpath={xpath_selector}").text_content()
            print(self.matchInfo['datetime'])

            # scheduler = []
            # try:
            #     locatorMatches = self.page.locator(f"xpath={self.xPathMatches}")
            #     logging.info(f"Успешное получение локатора на список из {locatorMatches.count()} участников матча")
            #     locatorDates = self.page.locator(f"xpath={self.xPathDates}")
            #     logging.info(f"Успешное получение локатора на список из {locatorDates.count()} даты матча")
            #     if (locatorMatches.count() != locatorDates.count()):
            #          raise Exception("Количество распознанных матчей не совпадает c количеством распознанных дат")
            #     for i in range(locatorMatches.count()):
            #         scheduler.append({'match' : locatorMatches.nth(i).text_content(), 'date' : locatorDates.nth(i).text_content() })
            #     return scheduler
            # except Exception as e:
            #     logging.error(e)
            #     raise
