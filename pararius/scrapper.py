from bs4 import BeautifulSoup
import requests
import logging
import time
# URL ='  https://www.pararius.com/apartments/amsterdam/sort-price-low'

# TODO: CHANHE TO SELENIUM TO GET ALL THE PAGES BS IS NOT WORKING

URL ='https://www.pararius.com/apartments/{area}/page-{page_number}/{sort}'


class para_scrapper:
    logging.basicConfig(level=logging.INFO)
    # FILEPATH = "datastore/houses/"
    
    # Variable for the links

    def __init__(self, sort, area, page_number,filename):
        self.area = area
        self.sort = sort
        self.filename = filename
        self.page_number = page_number
        self.FILEPATH= "datastore/houses/"

    def html_to_file(self, soup, filename,FILEPATH):
        with open(f"{FILEPATH}/{filename}.html", "w", encoding="utf-8") as f:
            f.write(str(soup))
            f.close()

    def create_url(self):
        return URL.format(area=self.area, sort=self.sort, page_number=self.page_number)

    def get_html(self):
        house_list = []
        response = requests.get(self.create_url())
        time.sleep(15)
        soup = BeautifulSoup(response.content, "html.parser")
        self.html_to_file(soup, filename='test',FILEPATH=self.FILEPATH)


para_scrapper = para_scrapper(sort="sort-price-low", area="amsterdam", page_number=1,filename="test")
print(para_scrapper.get_html())