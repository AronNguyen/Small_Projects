import discord
import asyncio

client = discord.Client()

@client.event
async def on_message(message):
    #we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.author.id == ('164077295173107712'):
        msg = "AI has become self aware"
        await client.send_message(message.channel, msg)

    if message.author.id == ('164075631196241920'):
        msg = "You've changed Francis"
        await client.send_message(message.channel, msg)

    if message.author.id == ('302944932547657738'):
        msg = "Hey fat ass"
        await client.send_message(message.channel, msg)

    

    if message.content.startswith("!hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTQwMDExMzMzNDcxNTY3OTA0.DzKsaQ.pFwe0jOApfaGOGLIo_QN6ebJJy0')
