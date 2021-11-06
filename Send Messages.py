from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

df = pd.read_excel("book.xlsx") #path of the excel file goes here
contacts = df["Contact Name"] #Name of the column curresponding to
messages = df["Message"] #message content

n = 3 

for i in range(n):
	target = ('"{}"'.format(contacts[i]))
	string = messages[i]

	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
		By.XPATH, x_arg)))
	group_title.click()
	inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
	input_box = wait.until(EC.presence_of_element_located((
		By.XPATH, inp_xpath)))

	input_box.send_keys(string + Keys.ENTER)
	time.sleep(1)