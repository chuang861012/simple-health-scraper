import requests
from lxml import etree
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

def getSearchResult(url,results=[]):
    print('scraping:',url)
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    links = html.xpath('//*[@id="container"]/div[1]/div[2]/main/div[2]/div/div/div/h3/a/@href')
    
    for link in links:
        results.append(getArticleContent(f'https://www.everydayhealth.com.tw{link}'))
        
    # goto next page
    next_page = html.xpath('//div[@class="pager"]/ul/li/a[text()=">"]/@href')
    if len(next_page) > 0:
        # delay 0.5 sec
        sleep(.5)
        return getSearchResult(next_page[0],results)
    else:
        return results

def getArticleContent(url):
    res = requests.get(url,headers=headers)
    content = res.content.decode()
    html = etree.HTML(content)
    
    title = html.xpath('//h1[@itemprop="headline"]/text()')
    date = html.xpath('//span[@itemprop="datePublished"]/text()')
    author = html.xpath('//span[@itemprop="author"]//text()')
    body = html.xpath('//div[@id="article_page"]//text()')
    
    return {
        'title':''.join(title),
        'date':''.join(date),
        'author':''.join(author),
        'body':''.join(body)
    }

if __name__ == "__main__":
    keyword = input('keyword:')
    data = getSearchResult(f'https://www.everydayhealth.com.tw/tag/{keyword}/1')
    print(data)