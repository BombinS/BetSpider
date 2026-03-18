import logging

class ClickSummary:
    
    def __init__(self, page):
        self.page = page
        self.xpath = "//a[contains(text(), 'Summary')]/.."
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info("Успешный клик на вкладку Summary")
            except Exception as e:
                logging.error(e)