import requests
from lxml import etree

url = "https://meiriyiwen.com/"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}


def get():
    res = requests.get(url=url, headers=headers).text

    tree = etree.HTML(res)

    article = tree.xpath('//*[@id="article_show"]')[0]

    title = article.xpath('./h1/text()')[0]

    author = article.xpath("./p[@class='article_author']/span/text()")[0]

    paragraph_list = article.xpath("./div[@class='article_text']/p/text()")

    return {
        "title": title,
        "author": author,
        "content": paragraph_list
    }
