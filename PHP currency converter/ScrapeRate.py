from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scrap:

    def __init__(self, site):
        self.site = urlopen(site).read()
        self.data = []
        self.raw_rate = []
        self.buy_rate = []
        self.sell_rate = []
        self.php_buy = dict([])
        self.php_sell = dict([])
        
    def get_data(self):
        buffer = ''
        sp = BeautifulSoup(self.site, 'html.parser')
        tags = sp.find_all('span')
        for item in tags:
            if item.get('class') == ['widget-exchange-rates__long-name']:
                for char in item.string:
                    if char == ' ' or char == '\n':
                        pass
                    else:
                        buffer += char
                self.data.append(buffer)
                buffer = ''
        tags = sp.find_all('td')
        for item in tags:
            if item.get('class') == ['widget-exchange-rates__price']:
                self.raw_rate.append(item.string)
        for index in range(0,len(self.raw_rate),2):
            self.buy_rate.append(self.raw_rate[index])
        for index in range(1,len(self.raw_rate),2):
            self.sell_rate.append(self.raw_rate[index])

        self.create_buy()
        self.create_sell()
    def create_buy(self):
        for index in range(len(self.data)):
            if self.data[index] not in self.php_buy.keys():
               self.php_buy[self.data[index]] = float(self.buy_rate[index])

    def create_sell(self):
        for index in range(len(self.data)):
            if self.data[index] not in self.php_sell.keys():
                self.php_sell[self.data[index]] = float(self.sell_rate[index])
