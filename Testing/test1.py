from urllib2 import Request, urlopen, URLError
import urllib2
from random import randint
from time import sleep

content = '2'

for i in xrange(1, 2):
    req = urllib2.Request('https://haveibeenpwned.com/api/v2/breachedaccount/idan.taler@gmail.com?truncateResponse=true')
    req.add_header('Accept', 'application/vnd.haveibeenpwned.v2+json')
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>')

    try:
        resp = urllib2.urlopen(req)
        content = resp.read()

        print content
        sleep(randint(2,3))

    except URLError, e:
        print 'No kittez. Got an error code:', e

print type(content)
for i in content:
    print i