from selenium.webdriver.chrome.options import Options

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.joox.com/id")
assert "Joox" in driver.title
driver.quit()
