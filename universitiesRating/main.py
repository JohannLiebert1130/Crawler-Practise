import requests
from bs4 import BeautifulSoup


class BestChinaUniv:
    def __init__(self):
        self.univ_list = []

    def get_html(self, url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            self.html = r.text
            return self.html
        except:
            print("Some error occurred when getting html")

    def fill_univ_list(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        trs = soup.find_all('tr', class_='alt')
        for tr in trs:
            tds = tr('td')
            self.univ_list.append([tds[0].string, tds[1].string, tds[3].string])

    def print_univ_list(self, num):
        print('Rating\tName\tScire')
        for i in range(num):
            univ_info = self.univ_list[i]
            print(f'{univ_info[0]}\t{univ_info[1]}\t{univ_info[2]}')

    def main(url, num):
        instance = BestChinaUniv()
        instance.get_html(url)
        instance.fill_univ_list()
        instance.print_univ_list(num)


if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    BestChinaUniv.main(url, 20)
