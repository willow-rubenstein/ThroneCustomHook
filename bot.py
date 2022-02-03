import twitter
from core import gift
import json

CONFIG = json.load(open('config.json'))
AUTH = json.load(open('auth.json'))

api = twitter.Api(consumer_key=AUTH['secret_auth']['api_key'],
                  consumer_secret=AUTH['secret_auth']['api_secret'],
                  access_token_key=AUTH['secret_auth']['access_token'],
                  access_token_secret=AUTH['secret_auth']['access_token_secret'],
                  sleep_on_rate_limit=True)

def listener():
    status = api.GetUserTimeline(screen_name=CONFIG['username'], count=1, include_rts=False, exclude_replies=True)[0].text
    print(gift.getParse(status))

listener()