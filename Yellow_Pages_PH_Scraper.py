'''
A program that scrapes company, telephone numbers,and address
on Yellow Pages Philippine Page.
'''
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Scrap:
    
    def __init__(self, x):
        self.company = []
        self.info = []
        self.html = urlopen(x).read()
        
    def scrape_company(self):
        sp = BeautifulSoup(self.html, 'html.parser') 
        for tag in sp.find_all('a'): #iterate from 'a' tag
            comp = tag.get('data-bizname')
            num = tag.get('data-phone')
            address = tag.get('data-bizadd')
            if isinstance(num,str) and isinstance(address, str):
                self.info = [comp,num,str(address)]
                self.company.append(self.info)
                self.info = [] 

    def show_nums(self):
        for item in self.company:
            print(item[1])

    def show_company(self):
        for item in self.company:
            print(item[0])

    def show_address(self):
        for item in self.company:
            print(item[2])

    def save_to_new(self):
        try:
            with open(input('Enter filename: ') + '.csv','w+') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerows(self.company)
        except:
            print('File name already in use.')
                    
    def save_to_existing(self):
        with open(input('Enter filename: ') + '.csv','a+') as file:
            writer = csv.writer(file, delimiter = ',')
            writer.writerows(self.company)
    
page = Scrap(input('Enter Yellow Pages PH url: '))
page.scrape_company()
