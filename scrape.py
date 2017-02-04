import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver = "/Users/Joel/Documents/Hacks/instaScrape/chromedriver"
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get("https://instagram.com")

loginElement = driver.find_element_by_class_name('_fcn8k').click()
# userElement = driver.find_element_by_css_selector('._kp5f7._qy55y')
# passEleement = driver.find_element_by_css_selector('._ccek6._i31zu')
userElement = driver.find_element_by_name('username')
passElement = driver.find_element_by_name('password')

userElement.send_keys('foodyhoodie')
sleep(0.2)
passElement.send_keys('B4ch0rm33')
sleep(0.2)
loginUserElement = driver.find_element_by_css_selector('._ah57t._84y62._i46jh._rmr7s')
loginUserElement.click()

#
sleep(0.5)
searchElement = driver.find_element_by_css_selector('._9x5sw._qy55y')
searchElement.send_keys('#cafeSG')
sleep(3)

driver.get("https://instagram.com/explore/tags/cafesg/")
