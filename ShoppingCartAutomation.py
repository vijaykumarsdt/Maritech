from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= "C:\\Users\\vijui\\chromedriver_87.0.4280.88_win32\\chromedriver.exe")

driver.get("https://www.amazon.co.uk/")
driver.maximize_window()
driver.implicitly_wait(1)


time.sleep(2)

driver.find_element_by_xpath('//*[@id="sp-cc-accept"]').click()
time.sleep(2)

# # Country
driver.find_element_by_xpath('//*[@id="icp-nav-flyout"]/span/span[2]').click()


# chenage the currency
driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]').click()

time.sleep(2)

#selectnewcurrency

driver.find_element_by_xpath('//*[@id="a-popover-1"]/div/div/ul/li[8]').click()
time.sleep(2)


driver.find_element_by_xpath('//*[@id="icp-btn-save"]/span/input').click()


driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys('Ipad')
driver.find_element_by_xpath('//*[@id="nav-search-submit-text"]/input').click()

driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span').click()

# Add to cart
driver.find_element_by_xpath('//*[@id="add-to-cart-button"]').click()
time.sleep(2)

#No thanks
driver.find_element_by_xpath('//*[@id="attachSiNoCoverage-announce"]').click()


# Assert checkout  cart

driver.find_element_by_xpath('//*[@id="attachDisplayAddBaseAlert"]/div/i').is_displayed()


print("Test Completed")


driver.quit()


