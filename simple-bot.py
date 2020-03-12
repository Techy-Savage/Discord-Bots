import discord
from discord.ext import commands
from datetime import datetime 
import asyncio

client = commands.Bot(command_prefix='.')

@client.command()
async def logs(ctx, arg):
    if arg == 'show':
        await ctx.send(file=discord.File('dislog.txt'))

@client.command()   
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount))


@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(u'Time:', dt_string, 'User:', message.author, 'ID:', message.author.id, 'Message:', message.content)
        with open('C:\\Users\\Techy\\Documents\\Python\\Bot\\dislog.txt', 'a', encoding="utf-8") as filed:
            filed.write(u'Time:, {}, User:, {}, ID:, {}, Message:, {} \n'.format(str(dt_string),str(message.author),str(message.author.id),str(message.content)))
        if '<@!668875024320430110>' in message.content:
            await message.channel.send("Don't @ me! <@{}>".format(message.author.id))
    await client.process_commands(message)

client.run('<Token>')
