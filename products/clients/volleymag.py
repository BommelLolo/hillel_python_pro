import logging
import requests
from requests import RequestException, HTTPError

from project.api_base_client import APIBaseClient
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def get_data(url_item, **kwargs):
    description = ''
    try:
        response = requests.request(
            method='get',
            url=url_item,
            **kwargs
        )

        soup_item = BeautifulSoup(response.content, 'html.parser')
        description_list = soup_item.find_all(
            'p', attrs={'style': 'text-align: justify;'})
        for part in description_list:
            description += part.text.replace('\n', '').replace("'", "")
    except (RequestException, HTTPError) as err:
        logger.error(err)
    return description


class VolleyMagSneakers(APIBaseClient):
    base_url = 'https://volleymag.com.ua/catalog/krosivki-dlja-volejboly/'
    site_url = 'https://volleymag.com.ua'

    def _prepare_data(self) -> list:
        self._request(
            'get',
        )
        results = []
        if self.response and self.response.status_code == 200:
            soup = BeautifulSoup(self.response.content, 'html.parser')
            category = soup.find('li', class_="breadcrumbs_item active").text
            for item in soup.find_all('div', class_="product_entity"):
                try:
                    url_item = item.find('a', class_="block-link").get('href')
                    url_item_full = ''.join([self.site_url, url_item])
                    image = ''. \
                        join([self.site_url,
                              item.find('img', class_="slide-img").get('src')])
                    price_text = item.find(
                        'span',
                        class_="product-price product-price--regular"
                    ).text
                    name = item.find('div', class_="product_title").text
                    name_clean = name.replace('\n', '')
                    description = get_data(url_item_full)
                    results.append({
                        'image': image,
                        'name': name_clean,
                        'description': description,
                        'price': price_text.split(' ')[0],
                        'category': category,
                        'sku': item.find(
                            'input',
                            attrs={"name": "cart[sku]"}).get('value')
                    })
                except Exception as err:
                    logger.error(err)
        return results

    def parse(self) -> list:
        return self._prepare_data()

    def get_image(self, url):
        self._request(
            'get',
            url=url
        )
        return self.response


parser_client = VolleyMagSneakers()
