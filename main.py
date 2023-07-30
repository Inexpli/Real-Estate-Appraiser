from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
import csv

# Selenium configuration
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
target = "https://bielsko-biala.nieruchomosci-online.pl/szukaj.html?3,mieszkanie,sprzedaz,,Bielsko-Bia%C5%82a:43459,,,,-4000000,,,,,,,1-9"
driver.get(target)

# InnerHTML -> .text() -> specifed fomat (number of rooms and floor level)
def extract_rooms_floor(text):
    rooms_pattern = r'Liczba pokoi:\s*(\d+)'
    floor_pattern = r'Piętro:\s*([^/]+)'

    num_rooms_match = re.search(rooms_pattern, text)
    floor_match = re.search(floor_pattern, text)

    num_rooms = num_rooms_match.group(1) if num_rooms_match else None
    floor = floor_match.group(1) if floor_match else None

    if floor == '-':
        floor = 0
    
    try:
        if num_rooms is not None:
            num_rooms = int(num_rooms)
    except ValueError:
        num_rooms = 0

    try:
        if floor is not None:
            floor = int(floor) if floor != 'parter' else 0
    except ValueError:
        floor = 0

    return num_rooms, floor

# Getting rid of units
def remove_units(text):
    units_to_remove = [" zł/m²", " zł", " m²"]
    for unit in units_to_remove:
        text = text.replace(unit, "")
    return text

# Replacing commas to dots (step to: string -> float)
def replace_commas_and_remove_spaces(text):
    text_without_commas = text.replace(",", ".")
    text_without_spaces = "".join(text_without_commas.split())
    return text_without_spaces

print("Scraping has been started...")

# Setting up the csv file
with open('estates.csv', 'a', newline='', encoding="utf-8") as csvfile:
    fieldnames = ['price', 'area', 'pricePerMeter', 'rooms', 'floor']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    csvfile.close()

# Website contains potentially 15 pages to scrape
pages = range(1, 16)
for page in pages:

    # On first page there are 48 estates to scrape
    # 1-48
    if page == 1:
        titles = range(1, 49)
    
    # 1-47
    elif page == 2 or page == 3 or page == 4:
        titles = range(1, 48)

    # 1-40
    elif page == 5:
        titles = range(1, 41)

    # On the rest of the pages there are 41 estates to scrape
    # 1-41
    else:
        titles = range(1, 42)

    print(f'Scraping page {page} out of 16')

    # single i in titles is referred to single offer on the site
    for i in titles:
        if i == 23 and page == 1: # Tile_23 on the first page works as ad that shouldn't be scraped
            pass
        else:
            xpath = f"//div[@id='tile_{i}']" #tile_1 , #tile_2 ...
            real_estates = driver.find_element("xpath", xpath)
            real_estates.click()
            # Getting price
            price = replace_commas_and_remove_spaces(remove_units(driver.find_element("xpath", "//span[@class='info-primary-price']").text))
            # Getting area
            area = replace_commas_and_remove_spaces(remove_units(driver.find_element("xpath", "//span[@class='info-area desktop-tablet-only']").text))
            # Getting price per meter
            pricePerMeter = replace_commas_and_remove_spaces(remove_units(driver.find_element("xpath", "//span[@class='info-secondary-price desktop-tablet-only']").text))
            # Getting the number of rooms and floor
            rest = driver.find_element("xpath", "//div[@id='attributesTable']").text
            rooms, floor = extract_rooms_floor(rest)
            with open('estates.csv', 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = ['price', 'area', 'pricePerMeter', 'rooms', 'floor']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'price': int(price), 'area': float(area), 'pricePerMeter': float(pricePerMeter), 'rooms':int(rooms), 'floor':int(floor)})
            driver.back()

    # Navigating to next page
    next_page = driver.find_element("xpath", "//span[@class='next']")
    next_page.click()
    # Waiting for website to load
    time.sleep(3)
csvfile.close()
print("Done!")