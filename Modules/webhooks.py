import time
import random
from random import choice
import names
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
import sys, os, platform
from os import system, name
from threading import Thread
from termcolor import colored, cprint
from datetime import datetime
import json
import urllib3
import re
import codecs
from requests.structures import CaseInsensitiveDict
from urllib.parse import urlencode
import urllib.parse
from urllib.parse import unquote
from anycaptcha import AnycaptchaClient, FunCaptchaProxylessTask, ZaloTask,AnycaptchaException
client = urllib3.PoolManager()
import threading 
import imaplib
import email
from time import sleep
from email.header import decode_header
os.system("")


def outlookpersonal(email, password, country):
    #pass
    try:
        webhook_url = "https://discordapp.com/api/webhooks/1015726492484911154/teNEI4wOlx_wH-bDl4igAkWZuXDPlMX54Fl93A73-36Ly929dbjzd-FhEpc8G3XZyGT1"
        pwebhook = DiscordWebhook(
        url=webhook_url,
        username= "TREX BOT",
        avatar_url="https://i.ibb.co/5LpkZ4p/B2-D84-D52-D2-CA-48-AC-BC02-9-BAEF01-C594-F.jpg"
    )
        embed = DiscordEmbed(title="Outlook Generator Module",color=517651)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/paXZmCWW1CXJa1kk1Zgl7xqkbIoFnR3CIkWsaisLK2Q/https/upload.wikimedia.org/wikipedia/commons/thumb/d/df/Microsoft_Office_Outlook_%25282018%25E2%2580%2593present%2529.svg/2000px-Microsoft_Office_Outlook_%25282018%25E2%2580%2593present%2529.svg.png?width=1126&height=1047")
        embed.add_embed_field(name='Email',value= email)
        embed.add_embed_field(name='Password',value= f"||{password}||")
        embed.add_embed_field(name='Country',value= country)
        embed.add_embed_field(name='SMS Serivce',value= ":x:")
        # embed.add_embed_field(name='Captcha Bypassed',value= "<:check:838456169546514464>")
        embed.set_footer(text='Outlook Generator Module')
        embed.set_timestamp()
        pwebhook.add_embed(embed)
        response = pwebhook.execute()
    except Exception as e:
        print(e)

def icloudpersonal(email):
    #pass
    try:
        webhook_url = "https://discordapp.com/api/webhooks/1015726492484911154/teNEI4wOlx_wH-bDl4igAkWZuXDPlMX54Fl93A73-36Ly929dbjzd-FhEpc8G3XZyGT1"
        pwebhook = DiscordWebhook(
        url=webhook_url,
        username= "TREX BOT",
        avatar_url="https://static.wikia.nocookie.net/logopedia/images/5/5e/Icloud.png/revision/latest?cb=20151107204136"
    )
        embed = DiscordEmbed(title="iCloud Generator Module",color=517651)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/ICloud_logo.svg/2560px-ICloud_logo.svg.png")
        embed.add_embed_field(name='Email Generated',value= email)
        # embed.add_embed_field(name='Captcha Bypassed',value= "<:check:838456169546514464>")
        embed.set_footer(text='iCloud Generator Module')
        embed.set_timestamp()
        pwebhook.add_embed(embed)
        response = pwebhook.execute()
    except Exception as e:
        print(e)



def yahoopersonal(name,email, password, country):
    try:
        webhook_url = "https://discordapp.com/api/webhooks/1015726492484911154/teNEI4wOlx_wH-bDl4igAkWZuXDPlMX54Fl93A73-36Ly929dbjzd-FhEpc8G3XZyGT1"
        pwebhook = DiscordWebhook(
        url=webhook_url,
        username= "TREX BOT",
        avatar_url="https://i.ibb.co/5LpkZ4p/B2-D84-D52-D2-CA-48-AC-BC02-9-BAEF01-C594-F.jpg"
    )
        embed = DiscordEmbed(title="Yahoo Generator Module",color=517651)
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Yahoo%21_%282019%29.svg/2560px-Yahoo%21_%282019%29.svg.png")
        embed.add_embed_field(name='Email',value= email)
        embed.add_embed_field(name='Password',value= f"||{password}||")
        embed.add_embed_field(name='Name',value= name)
        embed.add_embed_field(name='Region',value= country)
        embed.add_embed_field(name='SMS Serivce',value= "SMSACTIVATE")
        # embed.add_embed_field(name='Captcha Bypassed',value= "<:check:838456169546514464>")
        embed.set_footer(text='Yahoo Generator Module')
        embed.set_timestamp()
        pwebhook.add_embed(embed)
        response = pwebhook.execute()
    except Exception as e:
        print(e)


def prodirectpersonal(email, password, country):
    try:
        webhook_url = "https://discordapp.com/api/webhooks/1015726492484911154/teNEI4wOlx_wH-bDl4igAkWZuXDPlMX54Fl93A73-36Ly929dbjzd-FhEpc8G3XZyGT1"
        pwebhook = DiscordWebhook(
        url=webhook_url,
        username= "TREX BOT",
        avatar_url="https://i.ibb.co/5LpkZ4p/B2-D84-D52-D2-CA-48-AC-BC02-9-BAEF01-C594-F.jpg"
    )
        embed = DiscordEmbed(title="Prodirect Generator Module",color=517651)
        embed.set_thumbnail(url="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/v1457525788/pb7ecw65wfms8ciqx9gv.jpg")
        embed.add_embed_field(name='Email',value= email)
        embed.add_embed_field(name='Password',value= f"||{password}||")
        embed.add_embed_field(name='Country',value= country)
        # embed.add_embed_field(name='Captcha Bypassed',value= "<:check:838456169546514464>")
        embed.set_footer(text='Prodirect Generator Module')
        embed.set_timestamp()
        pwebhook.add_embed(embed)
        response = pwebhook.execute()
    except Exception as e:
        print(e)



def nikepersonal(email, password, country):
    #pass
    try:
        webhook_url = "https://discordapp.com/api/webhooks/1015726492484911154/teNEI4wOlx_wH-bDl4igAkWZuXDPlMX54Fl93A73-36Ly929dbjzd-FhEpc8G3XZyGT1"
        pwebhook = DiscordWebhook(
        url=webhook_url,
        username= "TREX BOT",
        avatar_url="https://i.ibb.co/5LpkZ4p/B2-D84-D52-D2-CA-48-AC-BC02-9-BAEF01-C594-F.jpg"
    )
        embed = DiscordEmbed(title="Nike Generator Module",color=517651)
        embed.set_thumbnail(url="https://www.everysize.com/mag/wp-content/uploads/nike-logo-swoosh-symbol.jpg")
        embed.add_embed_field(name='Email',value= email)
        embed.add_embed_field(name='Password',value= f"||{password}||")
        embed.add_embed_field(name='Country',value= country)
        embed.add_embed_field(name='SMS Serivce',value= "SMSACTIVATE")
        # embed.add_embed_field(name='Captcha Bypassed',value= "<:check:838456169546514464>")
        embed.set_footer(text='Nike Generator Module')
        embed.set_timestamp()
        pwebhook.add_embed(embed)
        response = pwebhook.execute()
    except Exception as e:
        print(e)

