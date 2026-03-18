import logging

class AcceptCookies:
    
    def __init__(self, page):
        self.page = page
        self.xpath = "//button[contains(text(), 'Accept')]"
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info("Успешный клик на согласие использования куков")
            except Exception as e:
                logging.error(e)