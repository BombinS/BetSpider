#!/bin/usr/env python

import sys, os, json, csv
from playwright.sync_api import sync_playwright

import logging
logging.basicConfig(filename='process.log', filemode='w', level=logging.INFO, encoding='utf-8')

# sys.path.append(os.path.dirname(__file__))
from config import target
from BetExplorerBasketballModules.goto_basketball_area import GoToBasketballArea
from BetExplorerBasketballModules.accept_cookies import AcceptCookies
from BetExplorerBasketballModules.click_summary import ClickSummary

def main():
    logging.info("Запуск баскетбольного парсера BetExplorer")
    
    # инициалицация Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()    

        GoToBasketballArea(page).process()
        AcceptCookies(page).process()
        ClickSummary(page).process()

        # кликнуть на название страны
        input()

        

if __name__ == "__main__":
    main()