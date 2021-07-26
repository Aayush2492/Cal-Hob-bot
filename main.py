import discord
import praw
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import os
from decouple import config

token_string = config('TOKEN')

#client = discord.Client()
client = commands.Bot(command_prefix='$')

# decorator functions


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

'''
@client.event
async def on_message(message):
    if message.author==client.user:
        return

    if message.content.startswith('$Goodbye'):
        await message.channel.send('Hello')
'''


def get_link_date(year_, month_, day_):
    r = requests.get('http://www.google.com')
    year = year_
    month = month_
    day = day_

    r = requests.get(
        f'https://www.gocomics.com/calvinandhobbes/{year}/{month}/{day}')

    print(r.status_code)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        tag = soup.find_all("picture", class_='item-comic-image')
        url = tag[0].img['src']
        return [url, r.status_code]
    else:
        return ['', 13]


def get_link():
    r = requests.get('http://www.google.com')
    year = 0
    month = 0
    day = 0
    while(1):
        year = random.randint(1985, 1995)
        month = random.randint(1, 12)
        day = random.randint(1, 31)
        r = requests.get(
            f'https://www.gocomics.com/calvinandhobbes/{year}/{month}/{day}')
        if r.status_code == 200:
            break

    soup = BeautifulSoup(r.content, 'lxml')
    tag = soup.find_all("picture", class_='item-comic-image')
    url = tag[0].img['src']
    return [url, year, month, day]


@client.command(name='calhob', help='Returns a strip from a random date')
async def calhob(ctx):
    [link, year, month, day] = get_link()
    await ctx.send(f"Calvin Hobbes Issue On: {day}/{month}/{year}\n"+link)


@client.command(name='calhob_on', help='calhob_on <day> <month> <year> - Returns strip on that date if exists :)')
async def calhob_on(ctx, day, month, year):
    [link, status_code] = get_link_date(year, month, day)
    if(status_code == 200):
        await ctx.send(f"Calvin Hobbes Issue On: {day}/{month}/{year}\n"+link)
    else:
        await ctx.send("Invalid Request!!!")

client.run(token_string)

'''
---------------Ignore------------------------------|
Reddit Part

client_secret = open("client_secret.txt","r").read()
client_id = open("client_id.txt","r").read()
password = open("password.txt","r").read()


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent="Anything",
    username="BoringGuy2492",
)

@client.command()
async def calhob(ctx):
    subreddit_name = "calvinandhobbes"
    subreddit = reddit.subreddit(subreddit_name)
    top = subreddit.top(limit=50)
    post_list = []
    for submission in top:
        post_list.append(submission)

    post_random = random.choice(post_list)
    title_of_post = post_random.title
    link_of_post = post_random.url
    await ctx.send(title_of_post+'\n'+link_of_post)
'''
