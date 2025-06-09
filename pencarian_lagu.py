driver.get("https://www.joox.com/id")
search_box = driver.find_element('name', 'search')
search_box.send_keys("Dewa 19")
search_box.submit()
assert "Dewa 19" in driver.page_source
