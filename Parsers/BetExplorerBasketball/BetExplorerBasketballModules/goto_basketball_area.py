import logging

class GoToBasketballArea:
    
    def __init__(self, page):
        self.page = page
        self.url = "https://www.betexplorer.com/basketball"
        self.wait_until = "domcontentloaded"

    def process(self):
            try:
                self.page.goto(self.url, wait_until=self.wait_until)
                logging.info("Успешный переход в раздел Баскетбол")
            except Exception as e:
                logging.error(e)