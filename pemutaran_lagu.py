driver.get("https://www.joox.com/id")
search_box = driver.find_element('name', 'search')
search_box.send_keys("Lagu Favorit")
search_box.submit()
driver.find_element('xpath', '//div[contains(@class,"song-item")][1]').click()
play_button = driver.find_element('class name', 'play-btn')
play_button.click()
assert "playing" in driver.page_source
