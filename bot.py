import twitter
from core import gift
import json
import asyncio
import websockets
from threading import Thread
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import tweepy

CONFIG = json.load(open('config.json'))
AUTH = json.load(open('auth.json'))

# Twitter-python sucks.     
tpy = tweepy.Client(bearer_token=AUTH['secret_auth']['bearer_token'])

# Set up discord webhook 
webhook = DiscordWebhook(url=AUTH['discord']['hook'], username="Throne Gifts", avatar_url="https://pbs.twimg.com/profile_images/1444450929244209152/sq068Mrt_400x400.jpg")

def sendHook(giftFrom, giftContaining, giftImage):
    embed = DiscordEmbed(title=f'New Gift From {giftFrom}', description=giftContaining, color='03b2f8')
    embed.set_image(url=giftImage)
    webhook.add_embed(embed)
    webhook.execute()

curWidget = ''
blacklist = []

api = twitter.Api(consumer_key=AUTH['secret_auth']['api_key'],
                  consumer_secret=AUTH['secret_auth']['api_secret'],
                  access_token_key=AUTH['secret_auth']['access_token'],
                  access_token_secret=AUTH['secret_auth']['access_token_secret'],
                  sleep_on_rate_limit=True)

def listener():
    global curWidget
    global blacklist
    while True:
        print("looping listener...")
        status = api.GetUserTimeline(screen_name=CONFIG['username'], count=1, include_rts=False, exclude_replies=True)[0]
        if status.id not in blacklist:
            print("New data found!")
            curWidget = gift.getParse(status.text)
            sendHook(curWidget['giftedFrom'], curWidget['giftName'], giftImage = f"https://pbs.twimg.com/media/{tpy.get_tweet(status.id, expansions='attachments.media_keys')[1]['media'][0].media_key.split('_')[1]}") #Ignore the image, it doesn't work rn
            blacklist.append(status.id)
        time.sleep(5)

Thread(target=listener).start()

async def runws(websocket, path):
    while True:
        await websocket.send(str(curWidget))
        await asyncio.sleep(5)

start_server = websockets.serve(runws, '127.0.0.1', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


