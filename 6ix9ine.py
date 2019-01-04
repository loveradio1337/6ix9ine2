import discord

from discord.ext import commands

from discord.ext.commands import Bot

import youtube_dl

import random

from os import environ

import asyncio

import time

import random

import datetime

import math

import requests


import random


import datetime

import math

import sys

import base64

import hashlib

import traceback

import string

import inspect

import json

import aiohttp

import websockets

import urllib.request

import logging

from collections import Counter

import os

import colorsys

import socket
from os import environ
from lxml import html
import asyncio
import time
import random
import datetime
import math
import requests
import sys
import base64
import hashlib
import traceback
import string
import inspect
import json
from cleverwrap import CleverWrap
import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket

bot = Bot(description="like is best", command_prefix=">")


print(f"Connecting your bot to discord!")
# remove help
bot.remove_command('help')

@bot.event
async def on_ready():
    print("STFU LETS GO!")
# help
@bot.command(pass_context=True)
async def test (ctx):
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKK")
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKK")
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKK")
    print("KKKKKKKKKKKKKKKKKKKKKKKKKKK")
    await bot.say("Bot is working...")
    await asyncio.sleep(1)
    await bot.say("Okay?")

@bot.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '🌟-welcome-🌟':
            embed = discord.Embed(color=0xC72323)
            embed.set_author(name="🎉 New member has joined 🎉", icon_url=member.avatar_url)
            embed.description = f'**Welcome ``{member.name}#{member.discriminator}`` to {member.server.name}**\n\nPlease 🙏 do not forget to respect each others and follow the rules.'
            embed.set_thumbnail(url=member.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_footer(text='We are now  {} members'.format(str(member.server.member_count)))
            await bot.send_message(channel, embed=embed)

@bot.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == '🌟-goodbye-🌟':
            embed = discord.Embed(color=0xC72323)
            embed.description = f"Peace out ``{member.name}#{member.discriminator}``✌!\n\nWe will gonna miss you in the ``{member.server.name}`` server."
            embed.set_author(name="👋 Member has left 👋", icon_url=member.avatar_url)
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_thumbnail(url=member.avatar_url)
            await bot.send_message(channel, embed=embed)

bot.run(os.environ['mytoken'])