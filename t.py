# coding=UTF-8
'''
暴力破解UNIX的密码,需要输入字典文件和UNIX的密码文件
'''

import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptPass == cryptWord:
            print('Found passed:', word)
            return
    print('Password not found!')

def main():
    passfile = open('passwords.txt','r')
    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1]
        print("Cracking Password For:", user)
        testPass(cryptPass)

if __name__ == '__main__':
    main()