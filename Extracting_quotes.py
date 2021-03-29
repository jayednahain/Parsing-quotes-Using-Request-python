
import requests
url = "https://quotes.toscrape.com/"
quotes_reponse = requests.get(url)

html_txt = quotes_response.text
pick_line='<span class="text" itemprop="text">'

clean_list = []
with open('quotes.txt','w') as f:
    for pick_line in html_txt:
        val=pick_line.replace('<span class="text" itemprop="text">','').replace('</span>','')
        #clear white spaces
        val=val.strip()
        clean_list.append(val)
        f.write(val)
        f.write('\n')