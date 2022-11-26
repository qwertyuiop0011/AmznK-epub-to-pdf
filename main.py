from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import config

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("headless")
options.add_argument("disable-gpu") 
options.add_argument("--no-sandbox")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

dv = webdriver.Chrome(chrome_options=options, executable_path=f'{config.CHROMEDRIVER_PATH}')
dv.set_window_size(1920, 1080)

dv.get(f'{config.KINDLE_BOOK_LINK}')
dv.find_element(by=By.XPATH, value='//*[@id="ap_email"]').send_keys(f'{config.AMAZON_KINDLE_USERNAME}')
dv.find_element(by=By.XPATH, value='//*[@id="ap_password"]').send_keys(f'{config.AMAZON_KINDLE_PASSWORD}')
dv.find_element(by=By.XPATH, value='//*[@id="signInSubmit"]').click()
time.sleep(8)
i=1

while True:
    element = dv.find_element(by=By.XPATH, value='//*[@id="main-content"]/div[1]/div/div[2]')
    dv.save_screenshot(f'res/{i}.png')
    ActionChains(dv).move_to_element(element).perform()
    dv.find_element(by=By.ID, value='kr-chevron-right').click()
    time.sleep(3)
    i = i+1