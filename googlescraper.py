import bs4
from urllib.request import urlopen as uReq, Request
from bs4 import BeautifulSoup as soup

def parse_url(url: str):
    # read url  
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    req = Request(url, headers=headers)
    uClient = uReq(req)
    
    page_html = uClient.read()
    uClient.close()

    # scrape page as html
    page_soup = soup(page_html, "html.parser")

    return page_soup

def get_lyrics(page_soup):
      
    # containerize
    containers = page_soup.find_all('div', {'class':'BNeawe tAd8D AP7Wnd'})
    lyrics = []
    
    
    for i in range(0, len(containers), 2):
        lyrics.append(containers[i].text)
    lyrics_str = "".join([str(x) for x in lyrics]).strip("\n")
    return lyrics_str

def get_artist(page_soup):
    # containerize
    containers = page_soup.find_all('span', {'class': 'BNeawe s3v9rd AP7Wnd'})
    return containers[1].text

def get_title(page_soup):
    # containerize
    containers = page_soup.find_all('span', {'class': 'BNeawe tAd8D AP7Wnd'})
    return containers[0].text

# print(get_artist(parse_url("http://www.google.com/search?q=black+holes+blue+ground+lyrics")))