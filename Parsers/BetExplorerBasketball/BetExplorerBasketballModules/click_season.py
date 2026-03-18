import logging

class ClickSeason:
    
    def __init__(self, page, target):
        self.page = page
        self.target = target
        self.xpath = f"//a[contains(@href, '{target}')]"
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info(f"Успешный клик на сезон {self.target}")
            except Exception as e:
                logging.error(e)