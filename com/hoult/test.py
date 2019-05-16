import re
import time
import requests
import urllib.request
from bs4 import BeautifulSoup

firefoxHead = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
IPRegular = r"(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])"
host = "https://blog.csdn.net"
url = "https://blog.csdn.net/hu_lichao/article/details/{}"

codes = ["82983127", "82990355", "82990200", "82658116", "82020121", "82990050", "82982895", "82982662", "82658116",
         "82982393", "82872754", "82726306", "82222074", "82019494", "80894466", "80895722",
         "80895400", "80895382", "80895361", "80895331", "80895117"]


def parseIPList(url="http://www.xicidaili.com/"):
    IPs = []
    request = urllib.request.Request(url, headers=firefoxHead)
    response = urllib.request.urlopen(request)
    soup = BeautifulSoup(response, "lxml")
    tds = soup.find_all("td")
    for td in tds:
        string = str(td.string)
        if re.search(IPRegular, string):
            IPs.append(string)
    return IPs


def PV(IP):
    s = requests.Session()
    s.headers = firefoxHead

    for i in range(len(codes)):
        print("No.{}\t".format(i), end="\t")
        s.proxies = {"http": "{}:8080".format(IP)}
        s.get(host)
        r = s.get(url.format(codes[i]))
        html = r.text
        print("html:",html)
        soup = BeautifulSoup(html, "html.parser")
        spans = soup.find_all("span")
        if len(spans) > 0:
            print(spans[2].string)
        time.sleep(2)


def main():
    IPs = parseIPList()
    for i in range(len(IPs)):
        print("正在进行第{}次访问\t".format(i), end="\t")
        print("\n")
        PV(IPs[i])


if __name__ == "__main__":
    main()