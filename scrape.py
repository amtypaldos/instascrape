import os
import sys
import getopt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import re

# chromedriver = "/Users/eric/instascrape/chromedriver"
driver = webdriver.Chrome()
# os.environ['webdriver.chrome.driver'] = chromedriver
# driver = webdriver.Chrome(chromedriver)



def scrape(username,password,hashtag):

    driver.get("https://instagram.com")

    loginElement = driver.find_element_by_class_name('_fcn8k').click()
    # userElement = driver.find_element_by_css_selector('._kp5f7._qy55y')
    # passEleement = driver.find_element_by_css_selector('._ccek6._i31zu')
    userElement = driver.find_element_by_name('username')
    passElement = driver.find_element_by_name('password')

    userElement.send_keys(username)
    sleep(0.2)
    passElement.send_keys(password)
    sleep(0.2)
    loginUserElement = driver.find_element_by_css_selector('._ah57t._84y62._i46jh._rmr7s')
    loginUserElement.click()

    #
    sleep(0.5)
    searchElement = driver.find_element_by_css_selector('._9x5sw._qy55y')
    searchElement.send_keys(hashtag)
    sleep(3)
    tag_wo_hash = re.sub('#', '', hashtag)
    hashurl = str("https://instagram.com/explore/tags/" + tag_wo_hash + "/")
    driver.get(hashurl)

    # Save the window opener (current window, do not mistaken with tab... not the same)
    # make main_window global
    global main_window
    main_window = driver.current_window_handle
    # Force to infinite scroll mode (click "Load more")
    driver.find_element_by_link_text('Load more').click()

def whatever(last_link):
    sleep(0.5)
    current_pointer = 0
    # Go to profile page
    recentPhotoElements = driver.find_elements_by_css_selector('._myci9 > a')
    for link in recentPhotoElements:
        current_pointer += 1
        # print(link)
        if current_pointer > last_link:
            # Open the link in a new tab by sending key strokes on the element
            # Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
            sleep(0.3)
            link.send_keys(Keys.COMMAND + Keys.SHIFT + Keys.RETURN)
            sleep(0.3)

            # Put focus on current window which will, in fact, put focus on the current visible tab
            driver.switch_to.window(driver.window_handles[1])

            # Click user profile link
            driver.find_element_by_css_selector('._f95g7 > a').click()
            try:
                bio = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "._bugdy > span"))
                )
                # Get inner text
                inner_text = driver.execute_script("return arguments[0].innerText;", bio)
                email_match = inner_text
                match = re.findall(r'[\w\.-]+@[\w\.-]+', email_match)
                print(inner_text)
                print('emails:', match)
            except TimeoutException:
                print("No bio")

            # Close current tab
            # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])

            # Put focus on current window which will be the window opener
            driver.switch_to_window(main_window)


    # Call self
    whatever(current_pointer)

# cli args
def main(argv):
   username = ''
   pw = ''
   hashtag = ''
   try:
      opts, args = getopt.getopt(argv,"u:p:t:",["username=","pw=","hashtag="])
   except getopt.GetoptError:
      print('scrape.py -u <username> -p <password> -t <hastag>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h' or opt == '--help':
         print('scrape.py -u <username> -p <password> -t <hastag>')
         sys.exit()
      elif opt in ("-u", "--username"):
         username = arg
      elif opt in ("-p", "--password"):
         pw = arg
      elif opt in ("-t", '--hashtag'):
         hashtag = arg

   scrape(username,pw,hashtag)

if __name__ == "__main__":
   main(sys.argv[1:])
whatever(0)
