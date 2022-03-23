import requests_html

ses = requests_html.HTMLSession()

# Element Methods #########################
res = ses.get('https://blog.python.org')
html = res.html
element = res.html.find('#Blog1 > div.blog-posts.hfeed > div:nth-child(1) > div > div > div > h3 > a', first=True)
element = res.html.xpath('//*[@id="Blog1"]/div[1]/div[1]/div/div/div/h3/a', first=True)

# GET ELEMENT TEXT
print(element.text)
# GET ELEMENT ATTRIBUTES
print(element.attrs)
print(element.attrs['href'])
# FIND ABSOLUTE URL
print(element.absolute_links.pop())
# GET ELEMENT TAG
print(element.tag)


# Pagination #########################
res = ses.get('https://blog.python.org')
html = res.html
for num,html in enumerate(res.html):
    if num <= 5:
        print(html)
    else:
        break


# Next Page #########################
res = ses.get('https://blog.python.org')
html = res.html
print(html)
res = ses.get(html.next())
html = res.html
print(html)


# Search  #########################  
res = ses.get('https://blog.python.org')
html = res.html
version = html.search('Major new features of the {version} series')['version']
print(version)


# Javascript #########################
from requests_html import AsyncHTMLSession

# RUN THIS IF YOU ARE USING JUPYTER NOTEBOOK
asession = AsyncHTMLSession()
res = await asession.get('https://www.w3schools.com/howto/howto_js_countdown.asp')
await res.html.arender()

# RUN THIS IF YOU ARE RUNNING CODE NOT IN JUPYTER NOTEBOOK
res = ses.get('https://www.w3schools.com/howto/howto_js_countdown.asp')
res.html.render()

# THIS CODE IS THE SAME FOR BOTH SCENARIOS
countdown = res.html.find('#countdown1', first=True).text
print(countdown)

