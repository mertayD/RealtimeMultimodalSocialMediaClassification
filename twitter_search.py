import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='
query = u'%23politics'
url = base_url + query

hashtag = "politics"
browser.get(f"https://twitter.com/search?q=+{hashtag}+&src=typed_query")
time.sleep(3)

results = []

list = browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
time.sleep(3)
print("count: " + str(len(list)))
for i in list:
    results.append(i.text)
loopCounter = 0
last_height = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    if loopCounter > 2:
        break
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(3)
    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    if last_height == new_height:
        break
    last_height = new_height
    loopCounter += 1

    list = browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")
    time.sleep(3)
    print("count: " + str(len(list)))

    for i in list:
        results.append(i.text)


count = 1
with open("tweets.txt", "w", encoding="UTF-8") as file:
    for item in results:
        file.write(f"{count}-{item}\n")
        count += 1
