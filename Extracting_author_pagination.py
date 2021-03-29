import requests
file_name = "1_to_10page_author_name.txt"
for page in range(1,11):
    target_url =f'https://quotes.toscrape.com/page/{page}/'
    quot_url_reponse = requests.get(target_url)
    html_data = quot_url_reponse.text
    with open(file_name,'w') as f:
        for lines in html_data.split('\n'):
            if author_tags in lines:
                value = lines.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
                value = value.strip()
                f.write(value)
                f.write('\n')
                print(value)