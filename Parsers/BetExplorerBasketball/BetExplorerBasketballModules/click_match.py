import logging

class ClickMatch:
    
    def __init__(self, page, xpath):
        self.page = page
        self.xpath = xpath
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info(f"Успешный клик на строку по локатору {self.xpath}")
            except Exception as e:
                logging.error(e)