import logging

# В этом классе логика. Активный чемпионат без плэй-офф этой вкладки не имеет.
# Отсутствие - валидное поведение, шаг просто пропускается и идем дальше
class ClickMainSeason:
    
    def __init__(self, page):
        self.page = page
        self.xpath = "//a[@title = 'Main season game statistics']"
        self.timeout = 5000

    def process(self):
            try:
                self.page.wait_for_selector(f"xpath={self.xpath}", timeout=self.timeout)
                self.page.click(f"xpath={self.xpath}")
                logging.info("Успешный клик на вкладку'Main season game statistics'")
            except Exception as e:
                logging.info("Вкладка 'Main season game statistics' не обнаружена")