# coding=UTF-8
import ftplib

def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
    except:
        dirList = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping To Next Target.')
        return
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if '.php' in fn or '.html' in fn or '.asp' in fn:
            print('[+] Found default page:' + fileName)
            retList.append(fileName)
    return retList

host = '123.56.99.154'#这个服务器是我买来学习的,大家不要玩的过火.
userName = 'anonymous'
passWord=''
ftp = ftplib.FTP(host)
ftp.login(userName,passWord)
print(returnDefault(ftp))
