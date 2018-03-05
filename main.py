import configparser
import json

import oandapyV20 as v20
import oandapyV20.endpoints.trades as trades

config = configparser.ConfigParser()
config.read("config.ini")
apiToken = config["Oanda"]["apiToken"]
accountID = config["Oanda"]["accountID"]

api = v20.API(access_token=apiToken)

r = trades.TradesList(accountID)

print("Request:{}".format(r))

resp = api.request(r)
print(type(resp))

print("Response:\n{}".format(json.dumps(resp["trades"], indent=2)))

print(resp["trades"][0]["id"])
tradeID = resp["trades"][0]["id"]

r = trades.TradeClose(accountID, tradeID)
api.request(r)




