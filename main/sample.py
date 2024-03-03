#import what we need
from requests_html import HTMLSession
session = HTMLSession()

r = session.get('https://www.indiatoday.in/crime')
def func(r):
    r.html.render(sleep=1, scrolldown=10)
    articles = r.html.find('article')
    newslist = []
    lst=[]
    for item in articles:
        try:
            newsitem = item.find('h2', first=True)
            title = newsitem.text
            newsitem = item.find('a', first=True)
            link = newsitem.absolute_links
            link=list(link)
            newsitem=item.find('img',first=True)
            img=newsitem.links
            lst=[newsitem.attrs]
            newsarticle = [
                title,
                 link[0] ,
                lst[0]['src']
            ]
            newslist.append(newsarticle)
        except:
            pass
    return newslist

