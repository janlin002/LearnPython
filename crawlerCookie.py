import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as req

def getData(url):
    request = req.Request(url, headers={
    "cookie": "over18=1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # beautifulsoup4
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    print(root.title.string)
    titles = root.find("div", class_ = "title")
    print(titles)
    print(titles.a.string)
    titless = root.find_all("div", class_ = "title")
    for item in titless:
        if item.a != None:
            print(item.a.string)
    nextLink = root.find('a', string="‹ 上頁")
    print(nextLink["href"])

url= 'https://www.ptt.cc/bbs/Gossiping/index.html'
getData(url);
