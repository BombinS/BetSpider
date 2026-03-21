import logging

from . click_ou import ClickOU 

class ObtainOUOdds:

    def __init__(self, page, matchInfo):
        self.page = page
        self.matchInfo = matchInfo

    def process(self):
        # кликнуть на вкладку O/U
        ClickOU(self.page).process()
        # получить тотал равных шансов (коэффициент на больше начинает превышать 1.81)