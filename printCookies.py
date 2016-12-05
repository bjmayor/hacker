import mechanize
import cookielib
'''
on my mac, fails:
mechanize._response.httperror_seek_wrapper: HTTP Error 403: request disallowed by robots.txt
'''
def printCookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)

    for cookie in cookie_jar:
        print(cookie)

url = 'https://www.baidu.com'
printCookies(url)