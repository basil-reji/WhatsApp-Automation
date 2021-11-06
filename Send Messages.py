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

imagepath = 'Full path of the image'

delay = 3 #delay in seconds

n = 3 #loop iteration count

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

	attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
	attachment_box.click()

	image_box = driver.find_element_by_xpath(
		'//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
	image_box.send_keys(imagepath)

	time.sleep(3)

	send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
	send_button.click()

	time.sleep(delay)
	search_bar = driver.find_element_by_class_name('_13NKt')
	search_bar.click()