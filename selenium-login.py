from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# chemin vers le driver

print("[Youssef] Starting test ...")
chrome_options = Options()
3zp$9!UdVi9N?J#4
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.saucedemo.com")
assert "Swag Labs" in driver.title
elem = driver.find_element(By.NAME, "user-name")
elem.clear()
elem.send_keys("standard_user")
elem2 = driver.find_element(By.NAME, "password")
elem2.clear()
elem2.send_keys("secret_sauce")
# Envoyer le formulaire de connexion
login_button = driver.find_element("css selector","#login-button")
login_button.click()
time.sleep(5)
assert "Login" not in driver.page_source

driver.close()


print("[Youssef] Finishing test ...")