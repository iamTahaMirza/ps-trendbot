from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import threading

driver = webdriver.Chrome()

driver.get("https://t.co/ZEOjvoh03m") # Link of presale page
time.sleep (5)

"""
Scrolling Functionality
"""
#####################################################################
def scroll():
    driver.execute_script("window.scrollTo(0,1000)")
    time.sleep (3)
    driver.execute_script("window.scrollTo(0,900)")
    time.sleep (2)
    driver.execute_script("window.scrollTo(0,1000)")
    time.sleep (1)
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep (3)
    driver.execute_script("window.scrollTo(0,700)")
    time.sleep (2)
    driver.execute_script("window.scrollTo(0,1100)")
    time.sleep (1)
    driver.execute_script("window.scrollTo(0,1300)")
    time.sleep (3)
    driver.execute_script("window.scrollTo(0,1000)")
    time.sleep (2)
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep (1)
    driver.execute_script("window.scrollTo(0,1100)")
    time.sleep (3)
    driver.execute_script("window.scrollTo(0,700)")
    time.sleep (2)
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep (1)
    driver.execute_script("window.scrollTo(0,900)")
    time.sleep (3)
    driver.execute_script("window.scrollTo(0,1200)")
    time.sleep (2)
    driver.execute_script("window.scrollTo(0,200)")
    time.sleep (5)

##########################################################################################################
"""
Links for xpaths of different social links for the projects.
"""

link1 = driver.find_element_by_xpath("(//a[@href='https://wizardzbsc.com/'])[1]")
link2 = driver.find_element_by_xpath("(//a[@href='https://twitter.com/WIZARDZBSC'])[1]")
link3 = driver.find_element_by_xpath("(//a[@href='https://t.me/Wizardzbsctoken'])[1]")
link4 = driver.find_element_by_xpath("(//a[@href='https://www.instagram.com/wizardzbsc/'])[1]")
# link6 = driver.find_element_by_xpath()
# link7 = driver.find_element_by_xpath()
# link8 = driver.find_element_by_xpath()

##########################################################################################################

"""
Link Click function & Return back to Pinksale page.
"""
def clickLink(link):
    link.click()
    time.sleep(7)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

##########################################################################################################

"""
Fill in the links and execute Bot.
"""
scroll()

clickLink(link1)
clickLink(link2)
clickLink(link3)
clickLink(link4)

                      
driver.quit()
