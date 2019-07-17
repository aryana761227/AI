from selenium import webdriver
import time

path_to_chromedriver = "chromedriver"  # enter path of chromedriver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)
url_esteghlal = 'https://twitter.com/FcEsteghlalIran'
url_perspolis = 'https://twitter.com/persepolisFC'

def tweet_scroller(url):
    browser.get(url)

    lastHeight = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(6)
        newHeight = browser.execute_script("return document.body.scrollHeight")

        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight

    html = browser.page_source

    return html
x = tweet_scroller(url_esteghlal)
Html_file = open("../esteghlal_page.html","w", encoding="utf-8")
Html_file.write(x)
Html_file.close()
y = tweet_scroller(url_perspolis)
Html_file = open("../perspolis_page.html","w", encoding="utf-8")
Html_file.write(y)
Html_file.close()