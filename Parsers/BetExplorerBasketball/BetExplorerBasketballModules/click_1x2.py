import logging

class Click1X2():

    def __init__(self, page):
        self.page = page
        self.xpath = "//a[@title = '1X2']"
        self.timeout = 5000
    
    def process(self):
        try:
            self.page.wait_for_selector(f"xpath={self.xpath}")
            self.page.click(f"xpath={self.xpath}")
            logging.info("Успешный клик на вкладку 1X2")
        except Exception as e:
            logging.error(f"Ошибка клика на вкладку '1X2' - {e}")