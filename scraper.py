from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set options
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Start driver
driver = webdriver.Chrome(options=options)

# Step 1: Go to login page
driver.get("https://www.gunz.com.au/customer/account/login/")

# Step 2: Log in
username = "your_username"
password = "your_password"

driver.find_element(By.ID, "email").send_keys(username)
driver.find_element(By.ID, "pass").send_keys(password)
driver.find_element(By.ID, "send2").click()
time.sleep(5)  # Wait for login

# Step 3: Go to a product category page
driver.get("https://www.gunz.com.au/catalog/category/view/id/74")  # example category
time.sleep(5)

# Step 4: Scrape first 5 products
products = driver.find_elements(By.CSS_SELECTOR, ".product-item-info")[:5]
for product in products:
    title = product.find_element(By.CSS_SELECTOR, ".product-item-link").text
    price = product.find_element(By.CSS_SELECTOR, ".price").text
    print(f"{title} - {price}")

driver.quit()
