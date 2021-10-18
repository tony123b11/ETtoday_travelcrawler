import requests
from bs4 import BeautifulSoup

page = input('請輸入瀏覽頁數：')


def web_html(page):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, "html.parser")
    get_title(soup)
    return(page)


def get_title(soup):
    result = soup.find_all("div", itemprop="itemListElement")
    for title in result:
        print(title.select_one("a").get("title"))
        print(title.select_one("a").get("href"))


try:
    page_count = int(page)
    for pages in range(1, page_count+1):
        print()
        # print("ETtoday旅遊雲,第"+str(pages)+"頁")
        search_herf = "https://travel.ettoday.net/category/%E5%8F%B0%E4%B8%AD/?&page="
        search_herf = search_herf+str(pages)
        test = web_html(search_herf)
        print("ETtoday旅遊雲,第"+str(pages)+"頁網址:"+test)

except:
    print("請輸入數字!")
