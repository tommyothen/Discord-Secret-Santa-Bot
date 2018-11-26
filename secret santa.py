import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import random


token = "" #TOKEN HERE

ownerID = "" #BOT OWNER ID HERE

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    elif message.content.startswith("-runRandom") and message.author.id == ownerID:
        memberList = []
        x = message.server.members
        for member in x:
            if member.id != client.user.id:
                memberList.append(str(member.id))
        random.shuffle(memberList)
        for i in range(0,len(memberList)-1):
            user = discord.utils.get(client.get_all_members(), id=memberList[i])
            if user is not None:
                messageContent = "You have been chosen to buy a gift for <@" + str(memberList[i+1]) + ">"
                await client.send_message(user, messageContent)
        user = discord.utils.get(client.get_all_members(), id=memberList[-1])
        messageContent = "You have been chosen to buy a gift for <@" + str(memberList[0]) + ">"
        await client.send_message(user, messageContent)
        await client.send_message(message.channel, "Randomised, chosen and sent all the messages!")


    elif message.content.startswith("-sendMessage") and message.author.id == ownerID:
        args = str(message.content).split(" ")
        remove = args.pop(0)
        memberList = []
        x = message.server.members
        for member in x:
            if member.id != client.user.id:
                memberList.append(str(member.id))
        random.shuffle(memberList)
        for i in range(0,len(memberList)-1):
            user = discord.utils.get(client.get_all_members(), id=memberList[i])
            if user is not None:
                await client.send_message(user, ' '.join(args))


@client.event
async def on_ready():
    print("Logged in as;")
    print("Name:",client.user.name)
    print("ID:  ",client.user.id)
    print("------------------------")
    print("Ready for gifts!")
    
client.run(token)
