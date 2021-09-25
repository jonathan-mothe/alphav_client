import requests

import settings

class APICallError(Exception):
    pass

class StockTimeSeries:

    def __init__(self):
        self.base_url = settings.BASE_URL
        self.api_key = settings.APIKEY

    def _build_url(self, path):
        return f"{self.base_url}?{path}&apikey={self.api_key}"

    def intraday_series(self, function, symbol, interval, **kwargs):

        path = f"function={function}&symbol={symbol}&interval={interval}"
        options = [f"{item[0]}={item[1]}" for item in kwargs.items()]
        path = f"{path}&{'&'.join(options)}" if options else path

        url = self._build_url(path)

        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()

        raise APICallError(
            f"Não foi possivel consumir o serviço: STATUS_CODE"
            "={resp.status_code}"
        )

    def daily_series(self, function, symbol, **kwargs):
        """
        1. Montar o path
        2. Gerar a URL
        3. Fazer a requisição ao AlphaVantage
        4. response.json()
        """

    def daily_adjusted_series(self, *args, **kwargs):
        """
        1. Montar o path
        2. Gerar a URL
        3. Fazer a requisição ao AlphaVantage
        4. response.json()
        """

    def weekly_series(self, *args, **kwargs):
        """
        1. Montar o path
        2. Gerar a URL
        3. Fazer a requisição ao AlphaVantage
        4. response.json()
        """
