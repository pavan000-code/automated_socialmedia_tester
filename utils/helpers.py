from selenium.webdriver.common.by import By

def login(driver, username, password):
    driver.get("https://www.facebook.com")
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.NAME, "login").click()
