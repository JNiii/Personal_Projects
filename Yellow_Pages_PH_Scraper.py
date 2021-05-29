from urllib.request import urlopen
from bs4 import BeautifulSoup



class Scrap:
    
    def __init__(self, x):
        self.company = []
        self.nums = []
        self.both = []
        self.html = urlopen(x).read()
        
    def scrape_company(self):
        sp = BeautifulSoup(self.html, 'html.parser') 
        for tag in sp.find_all('a'): #iterate from 'a' tag
            url = tag.get('data-section')
            #get data from data-section attribute in 'a' tag
            cname = tag.string
            #get data in between <a> </a>
            if url == 'business name': #double check if url attr has business name str
                self.company.append(cname)
                
    def scrape_num(self):
        sp = BeautifulSoup(self.html, 'html.parser')
        for tag in sp.find_all('a'): #iterate from 'a' tag
            url = tag.get('data-phone')
            if isinstance(url, str):
                self.nums.append(url)
               
    def scrape_both(self):
        for x in range(0,len(self.company)):
            self.both.append(self.company[x] + '\n' + 'tel:' + self.nums[x])
            print(self.both[x])\

    def show_company(self):
        for company in self.company:
            print(company)

    def show_nums(self):
        for tel_nums in self.nums:
            print(tel_nums)

    
scrap = Scrap('https://www.yellow-pages.ph/locations/quezon-city-metro-manila/page-2')
scrap.scrape_company()
scrap.scrape_num()
scrap.scrape_both()


