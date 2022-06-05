from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\python_selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
print("First test is completed")

driver.get("http://www.twitter.com")
print("twitter test is completed")

driver.get("http://www.gmail.com")
print("Gmail test is completed")
