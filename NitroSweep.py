import random, string
import requests
import colorama
import datetime
import discord
from dhooks import Webhook
import threading
colorama.init()
def sendWebhook (link):
    Found=discord.Color.from_rgb(255, 51, 255)

    hook=Webhook(webhook)
embed discord. Embed (
description
color=Found,
)
I
=
timestamp=datetime.datetime.utcnow(),
"Nitro Located!",
webhook =
embed.set author(name="V4C_ Scanner")
embed.add field (name="Link: ", value=str(link))
hook. send (embed=embed)
def onReady (amount) :
onReady
discord.Color.from_rgb (37, 114, 68)
"https://discord.com/api/webhooks/1051796221636919357/qM40827kDg2ThKoqCVVEx1-1Cs7vpFNPopzioY8RX nyzPwyUyB08DlrreVj39yjM