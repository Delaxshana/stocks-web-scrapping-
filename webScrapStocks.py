import requests
from bs4 import BeautifulSoup as bs
import time

start_time = time.time()
pages = []

for page_number in range(1,5):
    url_start = 'https://www.centralcharts.com/en/price-list-ranking/'
    url_end = 'ALL/desc/ts_20-us-tech-150--qc_3-previous-close-change?p='
    url = url_start + url_end + str(page_number)
    pages.append(url)


values_list = []
for page in pages:
    webpage = requests.get(page)
    soup = bs(webpage.text, 'html.parser')

    stock_table = soup.find('table', class_= 'tabMini tabQuotes')
    tr_tag_list = stock_table.find_all('tr')

    for each_tr_tag in tr_tag_list[1:]:
        td_tag_list =each_tr_tag.find_all('td')

        row_values = []
        for each_td_tag in td_tag_list[0:7]:
            new_value = each_td_tag.text.strip()
            row_values.append(new_value)

        values_list.append(row_values)

# to output txt file
file = open('stocks.txt','w')
for stock in values_list:
    file.write(str(stock) + "\n")
file.close()

# to output in csv file
df = pd.DataFrame(values_list)
df.to_csv('stocksData.csv', index=False, header=False)



