from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver=webdriver.Chrome(executable_path="C:\\python_selenium\\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("email")
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()

driver.implicitly_wait(4)
driver.find_element_by_name("password").send_keys("pass")
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()


#driver.find_element_by_name("login").click()
#print("FB")


