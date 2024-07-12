import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, \
    ElementClickInterceptedException
import pandas as pd

chrome_driver_path = "C:\\Development\\chromedriver.exe"


def get_data(search_term: str, location: str, sale_type: str):
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    browser = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(browser, 50)

    browser.get('https://www.ebay.co.uk')
    browser.maximize_window()

    search_bar = browser.find_element(By.ID, 'gh-ac')
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)

    if sale_type.lower() == "auction":
        auction_checkbox = browser.find_element(By.XPATH,
                                                "//input[@data-value='Auction']")
        auction_checkbox.click()
    elif sale_type.lower() == "bin":
        BIN_checkbox = browser.find_element(By.XPATH,
                                            "//input[@data-value='Buy it now']")
        BIN_checkbox.click()

    sold_checkbox = browser.find_element(By.XPATH,
                                         "//input[@aria-label='Sold items']")
    sold_checkbox.click()

    if location.lower() == "uk":
        UK_checkbox = browser.find_element(By.XPATH,
                                           "//input[@data-value='UK Only']")
        UK_checkbox.click()
    elif location.lower() == "eu":
        EU_checkbox = browser.find_element(By.XPATH,
                                           "//input[@data-value='European Union']")
        EU_checkbox.click()
    elif location.lower() == "ceu":
        CEU_checkbox = browser.find_element(By.XPATH,
                                            "//input[@data-value='Continental Europe']")
        CEU_checkbox.click()

    all_item_names = []
    all_item_prices = []
    all_item_dates = []
    all_bids = []
    all_conditions = []

    while True:
        item_names = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 's-item__title')))
        item_names_text = [item_name.text for index, item_name in
                           enumerate(item_names) if index > 1]
        all_item_names.extend(item_names_text)

        item_prices = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.POSITIVE')))
        item_prices_text = [item_price.text for index, item_price in
                            enumerate(item_prices) if index % 2 != 0]
        all_item_prices.extend(item_prices_text)

        item_dates = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.s-item__caption--signal.POSITIVE')))
        item_dates_text = [item_date.text for item_date in item_dates]
        all_item_dates.extend(item_dates_text)

        if sale_type.lower() == "auction":
            bids = wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '.s-item__bidCount')))
            bids_text = [bid.text for bid in bids]
            all_bids.extend(bids_text)
        else:
            # Fill bids with 'N/A' for Buy It Now items to maintain list length
            all_bids.extend(['N/A'] * len(item_names_text))

        conditions = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.s-item__subtitle .SECONDARY_INFO')))
        conditions_text = [condition.text for index, condition in
                           enumerate(conditions) if index > 1]
        all_conditions.extend(conditions_text)

        try:
            next_button = browser.find_element(By.XPATH,
                                               "//a[contains(@aria-label, 'Go to next search page')]")
            next_button.click()
            time.sleep(3)
        except (NoSuchElementException, ElementClickInterceptedException) as e:
            print("No more pages left or cannot click the next button.")
            break

    print("All Item Names length:", len(all_item_names))
    print("All Item Prices length:", len(all_item_prices))
    print("All Item Dates length:", len(all_item_dates))
    print("All Bids length:", len(all_bids))
    print("All Conditions length:", len(all_conditions))

    min_length = min(len(all_item_names), len(all_item_prices),
                     len(all_item_dates), len(all_bids), len(all_conditions))

    # Truncate all lists to the minimum length
    all_item_names = all_item_names[:min_length]
    all_item_prices = all_item_prices[:min_length]
    all_item_dates = all_item_dates[:min_length]
    all_bids = all_bids[:min_length]
    all_conditions = all_conditions[:min_length]

    all_data = {
        'Name': all_item_names,
        'Price': all_item_prices,
        'Date': all_item_dates,
        'Bids': all_bids,
        'Condition': all_conditions
    }

    df = pd.DataFrame(all_data)
    df['Name'] = search_term

    df['Type'] = 'Auction' if sale_type.lower() == "auction" else 'Buy it now'
    df['Location'] = {
        "uk": 'United Kingdom',
        "eu": 'European Union',
        "ceu": 'Continental Europe'
    }.get(location.lower(), 'Unknown')

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    return df


df1 = get_data('Charizard 4/102 base set', "UK", "Auction")
df2 = get_data('Charizard 4/102 base set', "EU", "Auction")

df3 = get_data('Blastoise 2/102 base set', "UK", "Auction")
df4 = get_data('Blastoise 2/102 base set', "EU", "Auction")

df5 = get_data('Venusaur 15/102 base set', "UK", "Auction")
df6 = get_data('Venusaur 15/102 base set', "EU", "Auction")

df7 = get_data('Charizard 4/102 base set', "UK", "BIN")
df8 = get_data('Charizard 4/102 base set', "EU", "BIN")

df9 = get_data('Blastoise 2/102 base set', "UK", "BIN")
df10 = get_data('Blastoise 2/102 base set', "EU", "BIN")

df11 = get_data('Venusaur 15/102 base set', "UK", "BIN")
df12 = get_data('Venusaur 15/102 base set', "EU", "BIN")

final_df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)
print(final_df)

final_df.to_csv("Auction_data.csv")
