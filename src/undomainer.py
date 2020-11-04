import requests
import sys
from optparse import OptionParser

def scanDomains(domain, port):
    sub_list = open("Wordlists/subdomains-10000.txt").read()
    subs = sub_list.splitlines()

    for word in subs:
        url = f"http://{word}.{domain}:{port}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:: ",url)

if __name__ == '__main__':
    # Set up options from the commandline
    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--port", dest="port",help="set target port to PORT", metavar="PORT", default="80")
    parser.add_option("-s", "--secure", dest="secure",help="Forces request to use SSL", default=False, action="store_true")
    parser.add_option(("-a"), "--https", dest="https",help="Scans using https", default=False  )
    parser.add_option("-t", "--target", dest="target",help="set target domain in format domain.top_level_domain", metavar="HOST")
    (options, args) = parser.parse_args()

    scanDomains(options.target, options.port)
        