from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present

chrome_options = Options()
chrome_options.add_argument("--disable-notification")

driver=webdriver.Chrome(executable_path="C:\\python_selenium\\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
driver.get("http://www.facebook.com")
driver.find_element_by_name("email").send_keys("email")
driver.find_element_by_name("pass").send_keys("pass")
driver.find_element_by_name("login").click()
print("FB")
