import urllib.parse

encoded = "%7B%22siteId%22%3A%221632%22%2C%22utm%22%3A%7B%22source%22%3A%22%22%2C%22medium%22%3A%22%22%2C%22campaign%22%3A%22%22%2C%22term%22%3A%22%22%2C%22content%22%3A%22%22%7D%2C%22site-session-id%22%3A%2291e251d2-4819-4993-8880-fc66eaeb07d1-5%22%7D"
decoded = urllib.parse.unquote(encoded)
print(decoded)