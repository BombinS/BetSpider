#!/bin/usr/env python

import json
from pathlib import Path
from playwright.sync_api import sync_playwright

import logging
logging.basicConfig(filename='process.log', filemode='w', level=logging.INFO, encoding='utf-8')

from config import target, links
from BetExplorerBasketballModules.goto_basketball_area import GoToBasketballArea
from BetExplorerBasketballModules.accept_cookies import AcceptCookies
from BetExplorerBasketballModules.click_summary import ClickSummary
from BetExplorerBasketballModules.click_country_name import ClickCountryName
from BetExplorerBasketballModules.click_season import ClickSeason
from BetExplorerBasketballModules.click_results import ClickResults
from BetExplorerBasketballModules.click_main_season import ClickMainSeason
from BetExplorerBasketballModules.get_schedule import GetSchedule
from BetExplorerBasketballModules.get_match_info import GetMatchInfo
from BetExplorerBasketballModules.validate_match_info import ValidateMatchInfo

def main():
    logging.info("Запуск баскетбольного парсера BetExplorer")
    
    # инициалицация Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()    

        # переход на отображение общей таблицы результатов
        GoToBasketballArea(page).process()
        AcceptCookies(page).process()
        ClickSummary(page).process()
        ClickCountryName(page, target, links).process()
        ClickSeason(page, target).process()
        ClickResults(page).process()
        ClickMainSeason(page).process()

        # получение информации [участники матча - дата матча]
        seasonInfo = {"season" : target, "schedule" :GetSchedule(page).process()}

        # получение информации для каждого матча
        for i in range(len(seasonInfo["schedule"])):    
            GetMatchInfo(page, seasonInfo["schedule"][i]).process()
            page.go_back(wait_until='commit')
            page.go_back(wait_until='commit')
            page.go_back(wait_until='commit')

        # сброс json
        with open(f"ParsedData/Basketball/{target}.json", "w", encoding="utf-8") as f:
            json.dump(seasonInfo, f)
                
        # валидация json 
        for match in seasonInfo["schedule"]:
            ValidateMatchInfo(match).process()

        # переносим лог
        try:
            s = Path("process.log")
            d = Path(f"ParsedData/Basketball/process_{target}.log")
            s.rename(d)
        except Exception as e:
            logging.error(f"Ошибка при переносе лога парсинга - {d.absolute}. Скорее всего файл открыт. {e}")

if __name__ == "__main__":

    main()