import logging

class ObtainDatetime:
    
    def __init__(self, page):
        self.page = page
        self.xpath = "//p[@id='match-date' and text() != '']"
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=5000)
                datetime = self.page.locator(f"xpath={self.xpath}").text_content()
                logging.info(f"Успешное получение даты и времени {datetime}")
                return datetime
            except Exception as e:
                logging.error(e)
                raise 