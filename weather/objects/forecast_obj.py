import re

compiled_date_regex = re.compile('(:\d\s)')

class Forecast(object):
    def __init__(self, forecast_data):
        self._forecast_data = forecast_data

    @property
    def text(self):
        return self._forecast_data['text']

    @property
    def date(self):
        if re.search(compiled_date_regex, self._forecast_data['date']):
            return re.sub(':',':0',self._forecast_data['date'])
        else:
            return self._forecast_data['date']
        
    @property
    def high(self):
        return self._forecast_data['high']

    @property
    def low(self):
        return self._forecast_data['low']

    @property
    def code(self):
        return self._forecast_data['code']

    @property
    def day(self):
        return self._forecast_data['day']
