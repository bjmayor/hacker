# coding=UTF-8
import ftplib
def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded!')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed!')
        return False


host = '123.56.99.154'#这个服务器是我买来学习的,大家不要玩的过火.
anonLogin(host)