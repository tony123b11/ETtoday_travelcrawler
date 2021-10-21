import requests
from bs4 import BeautifulSoup


def get_user_input():
    page = input('請輸入瀏覽頁數：')
    try:
        page_int = int(page)
       # print(type(page_int))
        return(page_int)
    except Exception as e:
        print(e)
        print("請輸入數字!")
        page_int = False
        return(page_int)


def print_result(page_result):
    for pages in range(1, page_result+1):
        # print("ETtoday旅遊雲,第"+str(pages)+"頁")
        search_herf = "https://travel.ettoday.net/category/%E5%8F%B0%E4%B8%AD/?&page="
        search_herf = search_herf+str(pages)
        test = web_html(search_herf, pages)
        # print(test[1])
        if test[1]:  # 如果回傳為空值直接跳出回全帶鰾後面幾頁沒有資料了!
            # print(test[1])
            if pages == page_result:
                print("一共"+str(pages)+"頁")
        else:
            print("一共"+str(pages-1)+"頁")
            break


def web_html(page, test):
    response = requests.get(page)
    soup = BeautifulSoup(response.text, "html.parser")
    exsist = get_title(soup)
    if exsist:
        # print("null")
        print("ETtoday旅遊雲,第"+str(test)+"頁網址:"+page)
        print()
    else:
        print()
    return(page, exsist)


def get_title(soup):
    result = soup.find_all("div", itemprop="itemListElement")
    # print(result)
    if not result:
        exsist_bool = False
        return(exsist_bool)
    else:
        exsist_bool = True
        for title in result:
            print(title.select_one("a").get("title"))
            print(title.select_one("a").get("href"))
        return(exsist_bool)


# 3
page = get_user_input()
bool = True
while bool:
    if page:
        # print(page)
        print_result(page)
        bool = False
    else:
        page = get_user_input()
        # print(type(page))

# print(type(page))
