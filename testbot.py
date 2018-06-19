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
        
        if "201405333195849729" in [role.id for role in message.author.roles]:
            print("Got command purge from", message.author)
            deleted = await bot.purge_from(message.channel, limit =x, check=None, before=None, after=None, around=None)
            await bot.send_message(message.channel, 'Deleted %s message(s)' % len((deleted)))
        else:
            await bot.send_message(message.channel, "You don't have permission to perform that command!")
            print("Denied request to purge channel from", message.author)
            
    if message.content.upper().startswith('!SCRIPTDELETE'):
        number = int(message.content.split()[1])
        if "201405333195849729" in [role.id for role in message.author.roles]:
            print("Got command scriptdelete from ", message.author, "\nNumber of messages: ", number)
            number = int(number) 
            counter = 0
            async for x in bot.logs_from(message.channel, limit = number):
                if counter < number:
                    await bot.delete_message(x)
                    counter = counter + 1
                    await asyncio.sleep(3.5)
            bot.send_message(message.channel, "Completed")
            print("Completed")
        else:
            await bot.send_message(message.channel, "You don't have permission to perform that command!")
    
                    
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
