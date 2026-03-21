import logging

class ClickOU:

    def __init__(self, page):
        self.page = page
        self.xpath = "//a[@title='Over/Under']"

    def process(self):
        try:
            self.page.wait_for_selector(f"xpath={self.xpath}")
            self.page.click(f"xpath={self.xpath}")
            logging.info("Успешный клик на вкладку Over/Under")
        except Exception as e:
            logging.error(f"Ошибка при клике на вкладку Over/Under - {e}")