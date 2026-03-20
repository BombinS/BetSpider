import logging

class ClickCountryName:
    
    def __init__(self, page, target, links):
        self.page = page
        self.countryName = ""
        try:
            for key, values in links.items():
                if target in values:
                    self.countryName = key
                    break
            if self.countryName == "":
                 raise KeyError(f"Наименование страны для цели {target} не найдено")
        except Exception as e:
             logging.error(e)

        self.xpath = f"//div[contains(@class, 'rightSidebar')]//a[contains(text(), '{self.countryName}')]"
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info(f"Успешный клик на наименование страны - {self.countryName}")
            except Exception as e:
                logging.error(e)