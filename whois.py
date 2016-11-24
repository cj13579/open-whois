import pythonwhois
import sys

def banner():
    print("* open-whois: 0.1.0")
    print("* Christopher Blake (cjb.blake@gmail.com), 2016")
    print("* https://github.com/cj13579/open-whois")  
    print(" ")

if len(sys.argv) < 2:
    banner()
    print"Nothing specified. Please specify a site name!"
    quit()

i = str(sys.argv[1])
domain = pythonwhois.get_whois(i)  
banner()
print(domain['raw'][0])