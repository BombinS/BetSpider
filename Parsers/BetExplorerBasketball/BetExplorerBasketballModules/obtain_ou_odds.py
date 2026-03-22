import logging

class ObtainOUOdds:

    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo
        self.xpath = "//td[@class='table-main__doubleparameter']"

    def process(self):
        try:
            # получить тотал равных шансов (коэффициент на больше начинает превышать 1.81)
            xpath_selector = self.xpath
            self.page.wait_for_selector(f"{xpath_selector}")
            totals = self.page.locator(f"{xpath_selector}")
            ktables = {}
            total = 0
            for j in range(totals.count()):
                total = totals.nth(j).text_content()
                kf = totals.nth(j).locator("xpath=following-sibling::td[1]").text_content().replace("\n","").replace(" ","")
                if total not in ktables:
                    ktables[total] = []
                ktables[total].append(kf)
            # бежим по словарю если в массиве коэффициентов длиной 3 и более среднее значение начинает превышать 1.81, считаем этот тотал истинным    
            for key in ktables:
                kfs = ktables[key]
                if len(kfs) < 3:
                    continue
                else:
                    float_kfs = [float(x) for x in kfs]
                    if sum(float_kfs) / len(float_kfs) < 1.81:
                        continue
                total = key
                break
            if total != 0 :
                logging.info(f"Успешное получение тотала - {total}")
                self.matchInfo['thresholdTotal'] = total
                self.matchInfo['thresholdTotalQuarter'] = round(float(total) / 4, 1)
            else:
                raise Exception()
        except Exception as e:
           logging.error(f"Неудачная попытка получения тотала - {e}")     