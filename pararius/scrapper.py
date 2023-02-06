from bs4 import BeautifulSoup
import requests
import logging

# URL ='  https://www.pararius.com/apartments/amsterdam/sort-price-low'

URL ='https://www.pararius.com/apartments/{area}/page-{page_number}/{sort}'


class para_scrapper:
    logging.basicConfig(level=logging.INFO)
    
    # Variable for the links
    URL = "https://www.linkedin.com/jobs/search/?keywords="
    FILEPATH = "datastore/"

    def __init__(self, sort, area, page_number):
        self.area = area
        self.sort = sort
        self.page_number = page_number

    def html_to_file(self, soup, filepath , filename):
        with open("{filepath}_{filename}.html", "w", encoding="utf-8") as f:
            f.write(str(soup))
            f.close()

    def create_url(self):
        return URL.format(area=self.area, sort=self.sort, page_number=self.page_number)

    def get_html(self, url):
        response = requests.get(url)
        return response.text

para_scrapper = para_scrapper(sort="sort-price-low", area="amsterdam", page_number=1)
print(para_scrapper.create_url())