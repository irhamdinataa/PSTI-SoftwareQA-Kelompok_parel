from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.joox.com/id/login")
driver.find_element('id', 'username').send_keys("test_user")
driver.find_element('id', 'password').send_keys("test_pass")
driver.find_element('id', 'login-button').click()
assert "dashboard" in driver.current_url
driver.quit()
