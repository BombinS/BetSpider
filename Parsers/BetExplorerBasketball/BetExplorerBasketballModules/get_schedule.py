import logging

class GetSchedule:
    
    def __init__(self, page):
        self.page = page
        self.xPathMatches = "//table[contains(@class, 'table-main')]//td[@class='h-text-left']//a"
        self.xPathDates = "//table[contains(@class, 'table-main')]//td[@class='h-text-right h-text-no-wrap']"

    def process(self):
            scheduler = []
            try:
                locatorMatches = self.page.locator(f"xpath={self.xPathMatches}")
                logging.info(f"Успешное получение локатора на список из {locatorMatches.count()} участников матча")
                locatorDates = self.page.locator(f"xpath={self.xPathDates}")
                logging.info(f"Успешное получение локатора на список из {locatorDates.count()} дат матчей")
                if (locatorMatches.count() != locatorDates.count()):
                     raise Exception("Количество распознанных матчей не совпадает c количеством распознанных дат")
                for i in range(locatorMatches.count()):
                    scheduler.append({'match' : locatorMatches.nth(i).text_content(), 'date' : locatorDates.nth(i).text_content() })
                return scheduler
            except Exception as e:
                logging.error(e)
                raise
