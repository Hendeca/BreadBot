import discord
import requests

import config
import datetime
import json
import random


async def hello(message):
    usage = 'Usage: !hello\n'
    message_arr = message.content.split(' ')
    if len(message_arr) > 1:
        await message.channel.send(usage)
        return
    else:
        await message.channel.send((
            "Hi there! I'm BreadBot. I was "
            "created by NealKongStrong. "
            "I'm here to provide you with stats about "
            f"{config.opensea['collection_title']}. "
            "You can type `!list` to see a list "
            "of all of my commands.\n\nHave fun!"))
        return


async def breadline(message):
    date_start = datetime.datetime.now() - datetime.timedelta(weeks=3)
    date_end = datetime.datetime.now()
    url = 'https://newsapi.org/v2/everything'
    url_params = {
        'q': ('(bread OR bagel OR loaf OR sandwich '
              'OR gluten OR rye OR "whole wheat" OR pita '
              'OR focaccia OR baguette OR croissant OR pastry)'
              ' NOT Russia NOT Ukraine'),
        'searchIn': 'title',
        'from': str(date_start)[:10],
        'to': str(date_end)[:10],
    }
    headers = {
        'X-Api-Key': config.news['api_key']
    }
    news_request = requests.get(
        url,
        headers=headers,
        params=url_params
    )
    if news_request.status_code == 200:
        data = news_request.json()
        articles = data['articles']
        article = random.choice(articles)
        embed = discord.Embed(
            colour=discord.Color.gold(),
            title=f"\"{article['title']}\"",
            description=article['description'],
            url=article['url']
        )
        embed.set_image(url=article['urlToImage'])
        await message.channel.send(embed=embed)
    else:
        await message.channel.send((
            "Oh gosh, I'm sorry. I couldn't get Bread news for you. "
            "Please forgive me <:breadpray:929291492026097684>\n\n"
            "We may have hit our 100 Bread News Items per Day Limit"
        ))


async def breadfact(message):
    with open('facts.json', 'r') as facts_file:
        data = facts_file.read()
    obj = json.loads(data)
    facts = obj['facts']
    fact = random.choice(facts)
    await message.channel.send(fact)


async def athensss(message):
    await message.channel.send('<:peeposuswut:933059026143567912>')


async def flee(message):
    author = f'<@{message.author.id}>'
    flee_messages = [
        (f"{author} just took off running on foot. "
         "They just jumped over someone's fence. They're "
         "entering a stranger's kitchen. They have taken "
         "a cat hostage. Police are in pursuit."),
        (f"{author} has stolen a car and is driving away from "
         "the scene into oncoming traffic. Oh, they've crashed into "
         "a minivan. They're exiting the vehicle and running on foot. "
         f"{author} is holding a 7 year-old at gunpoint. They've stolen "
         "a child's bike. Police are in pursuit."),
        (f"{author} has escaped on horseback. They are riding through "
         "the wide open plains. They are riding toward the sunset. From the "
         "police helicopter cam we can see what looks like a single tear "
         "running down their cheek. It looks like they've found inner peace. "
         "Turns out the city life wasn't what they really wanted. They wanted "
         "to commune with nature. Police are letting them live out the rest "
         "of their days in peace."),
        (f"{author} has climbed into an abandoned 747 jet. "
         "They are frantically drinking tiny "
         "bottles of liquor and pressing all "
         "of the flight attendent call buttons "
         "on the plane. Flight attendants "
         "are in a panic and can't keep up with all of the requests."
         "Police are scrambling jets."),
        (f"{author} has climbed into a submarine. They are diving deep, deep "
         "into the depths of the ocean. They have realized that, in truth, "
         "they always wanted to be a marine biologist. They're studying "
         "the aquatic lifeforms. The sub has gone too low for police to "
         "continue pursuit. They are never seen again...")]
    flee_message = random.choice(flee_messages)
    await message.channel.send(flee_message)


async def conspiracy(message):
    usage = ("You used this wrong dummy.\n"
             "Usage: `!conspiracy [list of @ mentions]`"
             "Try again and do better.\n")
    words = message.content.split(' ')
    if(len(words) == 1 or len(message.mentions) < 2):
        await message.channel.send(usage)
    else:
        accused = message.mentions
        author = message.author
        accused_string = ' '.join([f'<@{user.id}>' for user in accused])
        conspiracy = (
            f'<@{author.id}> has uncovered a conspiracy. '
            f'{accused_string} are all part of it. The dark money, '
            'the poisoned bread being sold on the streets, the mysterious '
            '"disappearances," it\'s all their doing! ALL OF IT!'
        )
        await message.channel.send(conspiracy)


async def accuse(message):
    usage = ("You used this wrong.\n"
             "Usage: `!accuse <username>`\n"
             "Plz try again")
    words = message.content.split(' ')
    if (len(words) != 2 or len(message.mentions) != 1):
        await message.channel.send(usage)
    else:
        accused = message.mentions[0]
        author = message.author
        accusation = (f'<@{author.id}> has accused '
                      f'<@{accused.id}> of a rly bad crime '
                      'that is highly illegal. I dunno what '
                      'they did, I\'m just a bot. But they '
                      'prolly should go to jail. Plz arrest them.')
        await message.channel.send(accusation)


async def list(message):
    embed = discord.Embed(
        colour=discord.Color.gold(),
        description=('A list of bot commands'),
        title='List of commands for BreadBot'
    )
    embed.add_field(
        name='!hello',
        value='Says hi to the bot',
        inline=False
    )
    embed.add_field(
        name='!list',
        value='Shows this list of bot commands!',
        inline=False
    )
    embed.add_field(
        name='!breadline',
        value='Displays a random, yet highly import, headline about bread',
        inline=False
    )
    embed.add_field(
        name='!breadfact',
        value='Displays a random bread fact so you can learn.',
        inline=False
    )
    embed.add_field(
        name="!ooh",
        value="Kongz together strong",
        inline=False
    )
    embed.add_field(
        name="!accuse <user>",
        value="Accuses a user of a terrible crime.",
        inline=False
    )
    embed.add_field(
        name="!conspiracy <list of users>",
        value="Accuse multiple users of taking part in a dark conspiracy.",
        inline=False
    )
    embed.add_field(
        name="!flee",
        value="Flee the scene. But we all know what you did.",
        inline=False
    )
    await message.channel.send(embed=embed)


async def ooh(message):
    await message.channel.send(
        'OOH AH AH!! KONG RISING AH AH... :banana:'
        )
