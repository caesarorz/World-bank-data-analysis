import requests


class URL:
    """Basic function to set up the WB url"""

    def __init__(self):
        self.indicator = ''
        self.country = ''
        self.url = ''

    def __str__(self):
        return f'{self}'

    def setIndicator(self, indicator):
        if indicator:
            self.indicator = indicator

    def setCountry(self, country):
        self.country = country

    def setUrl(self):
        self.url = f'http://api.worldbank.org/v2/country/{self.country}/indicator/{self.indicator}?format=json'

    def getIndicatorCountry(self):
        return {'country': self.country, 'indicator': self.indicator}

    def getURLIndicatorByCountry(self):
        return self.url


class FetchFilterAPI:
    """"Fetch to API and Generate information"""

    def __init__(self):
        self.api_info = ''
        self.url = URL()
        self.indicator_name = ''

    def setURL(self, url):
        self.url = url

    def fetchAPI(self):
        info = requests.get(self.url)
        self.api_info = info.json()[1:]

    def getInfo(self):
        return self.api_info

    def getIndicatorName(self):
        return self.indicator_name

    def setIndicatorName(self):
        self.indicator_name = self.api_info[0][1]['indicator']['value']

    def generateInfo(self):
        dict = {'year': [], f'{self.indicator_name}': []}
        for i in self.api_info[0]:
            if i['value']:
                dict['year'].append(i['date'])
                dict[self.indicator_name].append(i['value'])
        return dict
