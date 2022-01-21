import asyncio
import discord
import random
from datetime import datetime

from discord import embeds

# Client
bot = discord.Client()

# ROUSTANJE....


@bot.event
async def on_ready():
    borkohello = ['Borko online. Koga triba vozit doma?', 'Hippity Hoppity, woman are property',
                  'Jese ikome gleda ljubav je na selu?', 'Borko u kući', 'Stanići > Nemira. Change my mind',
                  'Alo mala, amo radit male Borčiće. Bit će lipi na mater', 'Alo mala, amo na  noćno kupanje, neće nas niko vidit']
    general_channel = bot.get_channel(704393952157106339)
    await general_channel.send(random.choice(borkohello))


@bot.event
async def on_disconnect():
    general_channel = bot.get_channel(704393952157106339)
    await general_channel.send('Ajte bok.')


@bot.event
async def background_loop():
    await bot.wait_until_ready()
    while not bot.is_closed:
        channel = bot.get_channel(704393952157106339)
        messages = ["Hello!", "How are you doing?", "Howdy!"]
        await bot.send_message(channel, random.choice(messages))
        await asyncio.sleep(2)

bot.loop.create_task(background_loop())


@bot.event
async def on_message(message):
    if (message.content == 'pog' or message.content == 'pogg' or message.content == 'poggg' or message.content == 'pogggg'):
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send('Šta je smišno mamlaze mali? Prikini pričat tako i ponašaj se normalno.')
        await general_channel.send('<:balt:823856424202928138>')

    if message.content == 'Ajde Borko dosta':
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send('<:MLGbaba:856528572718252063>')

    if (message.content == 'Borko' or message.content == 'borko'):
        borko = ['Štaje', 'E?', 'Reci', 'Ljubim te u oko',
                 'Ne mogu sad', '<:reltiHlieH:911651007732260874>']
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send(random.choice(borko))

    if (message.content == 'oće iko wt' or message.content == 'wt?'):
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send('Neću ja. Iđen leć.')

    if message.content == 'Borko šta si ti':
        general_channel = bot.get_channel(704393952157106339)
        borkoEmbed = discord.Embed(
            title="Ja san Borko", description="Dolazin iz Ruskamena", color=0xFF6100)
        borkoEmbed.add_field(name="Borko verzija", value="v1.0.0")
        borkoEmbed.add_field(name="Datum rođenja", value="15. 7. 2021.")
        borkoEmbed.set_footer(text="DUIDUIDUIDUIDUIDUI")
        borkoEmbed.set_author(name="Chad Roach")

    if (message.content == 'koliko je sati' or message.content == 'borko koliko je sati' or message.content == 'Borko koliko je sati' or message.content == 'Koliko je sati'):
        borkohours = ['Isto ka i jučer u isto doba',
                      'kOlIkO jE sAtI']
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send(random.choice(borkohours))

        await general_channel.send(embed=borkoEmbed)

    if "koliko je sati" in message.content:
        bhours = ['Šta koliko je sati?', 'Ne znan ja']
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send(random.choice(bhours))

    if "wt" or "war thunder" or "WT" in message.content:
        bhours = ['Ne mogu, iden na gradele',
                  'Ne mogu, brat mi u sobi ima koronu, a tamo je najbolji internet', 'Ne da mi se danas']
        general_channel = bot.get_channel(704393952157106339)
        await general_channel.send(random.choice(bhours))

# Run the client on the server
bot.run('ODY1MjgwMTgzNDE0MTYxNDM3.YPBs9w.smRH12YjBjDsyUb6G6RU_WAJ7fk')
