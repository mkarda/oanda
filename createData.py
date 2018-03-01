import configparser
import oandapyV20 as v20

import oandapyV20.endpoints.instruments as instruments

config = configparser.ConfigParser()
config.read("config.ini")
apiToken = config["Oanda"]["apiToken"]
accountID = config["Oanda"]["accountID"]

api = v20.API(access_token=apiToken)

params = {
    "count": 10,
    "from": '2017-03-22T19:00:00.000000000Z',
    "granularity": "H1",
}

req = instruments.InstrumentsCandles(instrument="EUR_USD", params=params)

res = v20.API.request(api, req)

print(res["candles"][0])
