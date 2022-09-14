import sys, os
import requests
import csv

if sys.platform.startswith('linux'):
    os.chdir(os.path.dirname(__file__))


# url = 'https://quotes.toscrape.com/'

# req = requests.get(url)

# print(req.status_code)

# html = req.text

# with open('quote_1st_page.txt', 'w') as txt:
#     for line in html.split('\n'):
#         if '<span class="text" itemprop="text">' in line:
#             line = line.replace('<span class="text" itemprop="text">', '')
#             line = line.replace('</span>', '').strip()
#             txt.write(line)
#             txt.write('\n')

# with open('author_1st_page.txt', 'w') as txt:
#     for line in html.split('\n'):
#         if '<small class="author" itemprop="author">' in line:
#             line = line.replace('<span>by <small class="author" itemprop="author">', '')
#             line = line.replace('</small>', '').strip()
#             txt.write(line)
#             txt.write('\n')

quotes = list()
authors = list()

for i in range(12):
    url = f'https://quotes.toscrape.com/page/{i}/'

    req = requests.get(url)

    print(f'Status:{req.status_code} Extracting HTML page {i+1}...........')

    html = req.text


    with open('quote_20_pages.txt', 'a') as txt:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“', '')
                quote = line.replace('”</span>', '').strip()
                quotes.append(quote)
                txt.write(line)
                txt.write('\n')

    with open('author_20_pages.txt', 'a') as txt:
        for line in html.split('\n'):
            if '<small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">', '')
                author = line.replace('</small>', '').strip()
                authors.append(author)
                txt.write(line)
                txt.write('\n')
    
with open('quotes.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Author', 'Quote'])
    # for quote, author in list(zip(quotes, authors)):
    #     field = {'Author': author, 'Quote': quote}
    #     writer = csv.DictWriter(csvfile, fieldnames=['Author', 'Quote'])
    #     writer.writerow(field)
    for quote, author in list(zip(quotes, authors)):
        field = [author, quote]
        writer = csv.writer(csvfile)
        writer.writerow(field)
    
