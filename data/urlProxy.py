import urllib.request

url = 'http://login.live.com'
proxy = urllib.request.ProxyHandler()
opener = urllib.request.build_opener(proxy)
print(opener.open(url).getcode())
