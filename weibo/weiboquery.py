# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:38:55 2015

@author: vincent
"""
from weibo import APIClient
import webbrowser
import urllib2

APP_KEY='2314407666'
APP_SECRET='51ba679c7b9fa76096df5f33a3532b49'
CALLBACK_URL='https://api.weibo.com/oauth2/default.html'

client=APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

url=client.get_authorize_url()
webbrowser.open_new(url)  
#login_url = 'https://api.weibo.com/oauth2/authorize' 
#
#url = client.get_authorize_url() 
#content = urllib2.urlopen(url) 
'''
if content:
    headers = { 'Referer' : url } 
request = urllib2.Request(login_url, params, headers) 
opener = get_opener(False) 
urllib2.install_opener(opener) 
try: 
    f = opener.open(request) 
    print f.headers.headers 
    return_callback_url = f.geturl 
# print f.read() 
except urllib2.HTTPError, e: 
    return_callback_url = e.geturl() 
# 取到返回的code 
print 
code = return_callback_url.split('=')[1] 
#得到token 
token = client.request_access_token(code)
'''
code=raw_input()
r=client.request_access_token(code)

access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)  

trends=client.trends__weekly()
trendslist=trends['trends']['2015-03-22 01:42']
for i in range(len(trendslist)):
    keys=trendslist[i].keys()
    values=trendslist[i].values()
    for j in range(len(trendslist[i])):
        print keys[j],values[j],'\n'


#statuses = client.statuses__public_timeline()['statuses']  
#length = len(statuses)  

#for i in range(0,length):  
#    print u'昵称：'+statuses[i]['user']['screen_name']  
#    print u'简介：'+statuses[i]['user']['description']  
#    print u'位置：'+statuses[i]['user']['location']  
#    print u'微博：'+statuses[i]['text']  
