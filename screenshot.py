from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\python_selenium\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
driver.save_screenshot("C:\python_selenium\seleniumscriptswithpython\hello.png")
print("Screenshot")
