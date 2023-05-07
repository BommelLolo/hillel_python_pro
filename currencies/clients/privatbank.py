from project.api_base_client import APIBaseClient


class PrivatBank(APIBaseClient):
    base_url = 'https://api.privatbank.ua/p24api/pubinfo'
    results = []
    """
    [{"ccy":"EUR","base_ccy":"UAH","buy":"40.50000","sale":"41.50000"},
    {"ccy":"USD","base_ccy":"UAH","buy":"37.10000","sale":"37.60000"}]
    output
    [{'code': 'USD', buy":"40.50000","sale":"41.50000"},
    ...
    ]
    """
    def prepare_data(self):
        self._request(
            'get',
            params={
                'json': '',
                'exchange': '',
                'coursid': 5
            }
        )
        self.results = []
        if self.response:
            for i in self.response.json():
                self.results.append({
                    'code': i['ccy'],
                    'buy': i['buy'],
                    'sale': i['sale']
                })


privatbank_client = PrivatBank()
