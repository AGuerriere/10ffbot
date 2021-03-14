# this is a Python script to get the highest score on 10fastfingers.

from selenium import webdriver
driver = webdriver.Chrome(executable_path="/Users/antonioguerriere/Applications/chromedriver")

#the following import allows the program to send text to the browser including enter.
from selenium.webdriver.common.keys import Keys
#this is needed for waiting for the page to fully load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get('https://10fastfingers.com/typing-test/english')

# click allow cookies
time.sleep(4)
try:
    element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection'))
    )
    element.click()
except:
    driver.quit()
def typer():
    for i in range(370):
            current_word = driver.find_element_by_class_name("highlight").text
            print(current_word)
            driver.find_element_by_class_name("form-control").send_keys(current_word)
            driver.find_element_by_class_name("form-control").send_keys(u'\ue00d')


typer()