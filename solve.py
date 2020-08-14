import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
#driver = TorBrowserDriver("/home/aravindha/Downloads/tor-browser-linux64-9.5.1_en-US/tor-browser_en-US")
driver.get("http://127.0.0.1:8000/")
driver.find_element_by_xpath('/html/body/center/button').click()
src=driver.page_source
soup = BeautifulSoup(src,"html.parser")
#time.sleep(1)
soup = soup.find("div",{"id":"test"})
text = soup.find_all("span")
typing=""
for i in range(len(text)):
	regex = r'<span style=\"order: {}; >(.*?)<\/span>'.format(i)
	match = re.findall(regex,str(text))[0].replace("\\xa0","")
	typing+=str(match).strip().replace(" ","")+' '

textbox = driver.find_elements_by_tag_name('textarea')[0]

js='document.getElementsByTagName(\"textbox\").innerText=\'{}\''.format(typing)
for i in typing:
	actions = ActionChains(driver)
	if i == ' ':
		actions.send_keys(Keys.SPACE)
		actions.send_keys(Keys.BACKSPACE)
		#actions.send_keys(Keys.BACKSPACE)
		#time.sleep(0.01)
	actions.send_keys(i)
	print(i,end="")
	actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
actions = ActionChains(driver)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
