from pprint import pprint
import requests

bot_token = "510212092:AAFDl0xXfTy0qaAfnZdCcN6tkYoA7gZgFF0"
test_url = "https://9e17395c.ngrok.io/{}".format(bot_token)

def get_url(method):
    return "https://api.telegram.org/bot{}/{}".format(bot_token,method)

r = requests.get(get_url("setWebhook"), data={"url": test_url})
r = requests.get(get_url("getWebhookInfo"))
pprint(r.status_code)
pprint(r.json())

