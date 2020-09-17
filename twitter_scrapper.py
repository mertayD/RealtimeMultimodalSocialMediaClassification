import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='
query = u'%23politics'
url = base_url + query

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_class_name('css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
temp = browser.find_elements_by_css_selector("span[class='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0']")
print(tweets)
#print(temp)
#class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"
#class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"
for tweet in temp:
    if(tweet.text != ""):
        print(tweet.text)
# PATH AFTER GETTING TO MULTIPLE DIV PART div/div/article/div/div/div/div[2]/div[2]/div[2]/div/div/span
