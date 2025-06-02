import undetected_chromedriver as uc
import pandas as pd
import time
from selenium.webdriver.common.by import By

# Setup headless stealth driver
options = uc.ChromeOptions()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = uc.Chrome(options=options)

# STEP 1: Login to Gunz
driver.get("https://www.gunz.com.au/login")
time.sleep(3)

# Login (replace with your real credentials)
driver.find_element(By.ID, "Email").send_keys("intern7@dentalfoundation.org.au")
driver.find_element(By.ID, "Password").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# STEP 2: Go to products page
driver.get("https://www.gunz.com.au/shop/category/oral-care-toothbrushes")
time.sleep(5)

# STEP 3: Scrape 5 products
products = driver.find_elements(By.CSS_SELECTOR, ".product-box")[:5]
data = []

for product in products:
    try:
        title = product.find_element(By.CSS_SELECTOR, ".product-title").text
        price = product.find_element(By.CSS_SELECTOR, ".price").text
        data.append({"Title": title, "Price": price})
    except:
        continue

driver.quit()

# Show as table
df = pd.DataFrame(data)
print(df)
