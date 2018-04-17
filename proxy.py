from browsermobproxy import Server

server = Server("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/browsermobproxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("google")
driver.get('http://login.live.com/')
print(proxy.har)

proxy.stop()
driver.quit()
