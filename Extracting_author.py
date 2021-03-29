import requests
url = "https://quotes.toscrape.com/"
quot_url_reponse = requests.get(url)
html_data = quot_url_reponse.text


author_tags = '<span>by <small class="author" itemprop="author">'
with open('author_names.txt','w') as f:
    for lines in html_data.split('\n'):
        if author_tags in lines:
            value = lines.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            value = value.strip()
            f.write(value)
            f.write('\n')