import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Setup Chrome options for Binder
options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Launch headless Chrome
driver = uc.Chrome(options=options)

# Step 1: Log in to Gunz (replace with your real login details)
driver.get("https://www.gunz.com.au/login")
time.sleep(3)

driver.find_element(By.ID, "Email").send_keys("intern7@dentalfoundation.org.au")
driver.find_element(By.ID, "Password").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# Step 2: Visit product page
driver.get("https://www.gunz.com.au/shop/category/oral-care-toothbrushes")
time.sleep(5)

# Step 3: Extract 5 product details
products = driver.find_elements(By.CSS_SELECTOR, ".product-box")[:5]
results = []

for p in products:
    try:
        name = p.find_element(By.CSS_SELECTOR, ".product-title").text
        price = p.find_element(By.CSS_SELECTOR, ".price").text
        results.append({"Title": name, "Price": price})
    except Exception as e:
        print("Error reading product:", e)

driver.quit()

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("products.csv", index=False)
print(df)
