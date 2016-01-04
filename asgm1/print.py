import urllib
import json

response=urllib.urlopen("https://api.weibo.com/2/trends/hourly.json")

print json.load(response)