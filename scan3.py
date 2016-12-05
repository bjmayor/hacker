# coding=UTF-8
import optparse
import nmap
'''
python scan3.py -H 14.215.177.38 -p 21 23 80 443 8080
'''

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, tgtPort)
    state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
    print (" [*] " + tgtHost + " tcp/" + tgtPort + " " +state)

def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -p <target host>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest = 'tgtPort', type='int', help='specify target port')
    options, args = parser.parse_args()
    if options.tgtHost is None or options.tgtPort is None:
        print(parser.usage)
        exit(0)
    else:
        tgtHost = options.tgtHost
        tgtPort = options.tgtPort
    args.append(tgtPort)
    for port in args:
        nmapScan(tgtHost, str(port))

if __name__ == '__main__':
    main()