# coding=UTF-8
'''
用字典暴力破解ZIP压缩文件密码,命令行指令zip文件和密码文件
'''
import zipfile
import threading
import optparse

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("Found Passwd:", password)
        return password
    except:
        pass

def main():
    parser = optparse.OptionParser('usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest = 'dname', type='string', help='specify dictionary file')
    options, args = parser.parse_args()
    if options.zname is None or options.dname is None:
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname


    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
