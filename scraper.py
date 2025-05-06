# scraper.py
from playwright.sync_api import sync_playwright
import time

def scrape_cfe_receipt(rpu_number):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://app.cfe.mx/aplicaciones/CCFE/SolicitudesCFE/Solicitudes/ConsultaTuReciboLuzGmx")

        # Example interaction; update with real selectors
        page.fill('#txtRPU', rpu_number)
        page.click('#btnBuscar')
        
        page.wait_for_timeout(5000)  # Better: wait_for_selector

        # Scrape output
        result_text = page.inner_text("#resultado")

        browser.close()
        return {'rpu': rpu_number, 'result': result_text}

