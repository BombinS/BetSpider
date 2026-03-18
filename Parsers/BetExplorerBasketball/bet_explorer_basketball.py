#!/bin/usr/env python

import sys, os, json, csv
from playwright.sync_api import sync_playwright

import logging
logging.basicConfig(filename='process.log', filemode='w', level=logging.INFO, encoding='utf-8')

from config import target, links
from BetExplorerBasketballModules.goto_basketball_area import GoToBasketballArea
from BetExplorerBasketballModules.accept_cookies import AcceptCookies
from BetExplorerBasketballModules.click_summary import ClickSummary
from BetExplorerBasketballModules.click_country_name import ClickCountryName
from BetExplorerBasketballModules.click_season import ClickSeason

def main():
    logging.info("Запуск баскетбольного парсера BetExplorer")
    
    # инициалицация Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()    

        GoToBasketballArea(page).process()
        AcceptCookies(page).process()
        ClickSummary(page).process()
        ClickCountryName(page, target, links).process()
        ClickSeason(page, target).process()

        input()

if __name__ == "__main__":
    main()