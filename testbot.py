import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from random import randint
import logging

Bot = discord.Client()
bot = commands.Bot (command_prefix = "!")
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print("Bot is online and ready to take commands")

@bot.command()
async def roll(x: int,y: int):
    z = randint(x, y)
    await bot.say("Rolling from %s and %s returned a %s" % (x,y,z))

@bot.command()
async def test(x):
    await bot.say(x)

@bot.event
async def on_message(message):
    if message.content.upper().startswith('!PURGE'):
        x = int(message.content.split()[1])
        y = message.author.roles
        
        if "419588713207824394" in [role.id for role in message.author.roles]:
            print("Got command clear from", message.author)
            deleted = await bot.purge_from(message.channel, limit =x)
            await bot.send_message(message.channel, 'Deleted %s message(s)' % len((deleted)))
    #if message.content.upper().startswith('!SLAP') slap command
    

''' purge command?
@bot.command()
async def purge(x):
    bot.say()
    if  "457943777382891522" == discord.Role.id:
        print("Got command clear from", discord.author)
        deleted = await bot.purge_from(discord.channel, limit =x)
        await bot.say('Deleted %s message(s)' % len((deleted)))
    else:
        bot.say("You do not have permissions to execute that command!")

'''


    

bot.run("")


