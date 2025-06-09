driver.get("https://www.joox.com/id/vip")
driver.find_element('id', 'subscribe-button').click()
driver.find_element('id', 'credit-card-number').send_keys("4111111111111111")
driver.find_element('id', 'expiry-date').send_keys("12/30")
driver.find_element('id', 'cvv').send_keys("123")
driver.find_element('id', 'confirm-payment').click()
assert "Premium Member" in driver.page_source
