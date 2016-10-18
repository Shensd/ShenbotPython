import discord
import asyncio
import json
import time
import random
import threading

#local files
import general
import people
import terminal

client = discord.Client()

#voteskip variables
voteGoing = False
votesYes = 0
votesNo = 0
votesRequired = 0
usersVoted = [None]

with open('assets/json/login.json') as data:
    login = json.load(data)

async def send_file(message, filePath):
    with open(filePath, 'rb') as f:
        await client.send_file(message.channel, f)
    print(">> {} sent in '{}'".format(filePath, message.channel))

async def endVote(message):
    await asyncio.sleep(5)
    await client.send_message(message.channel, "Vote will end in 10 seconds")
    await asyncio.sleep(5)
    await client.send_message(message.channel, "Vote will end in 5 seconds")
    await asyncio.sleep(5)

    global votesRequired
    global usersVoted
    global votesNo
    global votesYes
    global voteGoing
    await client.send_message(message.channel, "The vote has ended, tallying votes...")
    if votesYes > votesNo:
        await client.send_message(message.channel, "The song will be skipped")
        await client.send_message(message.channel, "-skip")
    elif votesNo > votesYes:
        await client.send_message(message.channel, "The song will not be skipped")
    elif votesNo == votesYes:
        await client.send_message(message.channel, "There is a tie! Tails means skip, heads means no skip.")
        await client.send_message(message.channel, "Flipping a coin...")
        random.seed(time.time())
        if random.randint(1, 2) == 1:
            await client.send_message(message.channel, "The coin has landed tails, the song will be skipped")
            await client.send_message(message.channel, "-skip")
        else:
            await client.send_message(message.channel, "The coin has landed heads, the song will not be skipped")
    votesRequired = 0
    votesYes = 0
    votesNo = 0
    voteGoing = False
    del usersVoted[:]


@client.event
async def on_ready():
    print(">> Logged in as {}, {}".format(client.user.name, client.user.id))
    print(">> {} is ready.".format(client.user.name))
    terminal.start_term()

@client.event
async def on_message(message):

    if not message.content[:1] == "$":
        return
    else:
        print(">> {} : {}".format(message.author.name, message.content))

    cmd = message.content.lower()[1:]
    base = cmd.split(" ")[0]
    try:
        option = cmd.split(" ")[1]
    except IndexError:
        option = None

    #Other Files
    await general.command(message, base, client)
    await people.command(message, base, client)

    #Other
    if base == 'reeses':
        await client.send_message(message.channel, "This command currently doesn't work")
    if base == 'summon':
        print(message.author.voice_channel)
        if client.voice_client_in(message.server):
            try:
                await client.move_member(client.user, message.author.voice_channel)
            except (discord.InvalidArgument, asyncio.TimeoutError, discord.ClientException):
                pass
        else:
            try:
                await client.join_voice_channel(message.author.voice_channel)
            except (discord.InvalidArgument, asyncio.TimeoutError, discord.ClientException):
                pass
        return
    #Commands that require options
    if base == 'voteskip':
        if terminal.noGod:
            await client.send_message(message.channel, "You have no god, voteskip is disabled.")
            return

        global usersVoted
        global voteGoing
        global votesYes
        global votesNo
        if option == "start":
            if not voteGoing:
                voteGoing = True
                await client.send_message(message.channel, "{} a vote has been started, vote with $voteskip OPTION".format(message.server.default_role))
                await client.send_message(message.channel, "Vote will end in 15 seconds")

                await client.send_message(message.channel, "{} You have voted yes".format(message.author.mention))
                votesYes+=1
                usersVoted.append(message.author)

                await endVote(message)
            else:
                await client.send_message(message.channel, "{} a vote is already going!".format(message.author.mention))
        if (option == "yes") or (option == "no"):
            if not voteGoing:
                await client.send_message(message.channel, "{} A vote is currently not going, start one with $voteskip start".format(message.author.mention))
                return
            for user in usersVoted:
                if user == message.author:
                    await client.send_message(message.channel, "{} You have already voted!".format(message.author.mention))
                    return
            if option == "yes":
                votesYes+=1
                await client.send_message(message.channel, "{} You have voted yes".format(message.author.mention))
            else:
                votesNo+=1
                await client.send_message(message.channel, "{} You have voted no".format(message.author.mention))
            usersVoted.append(message.author)
            return
    if base == 'shoot':
        if option == None:
            await client.send_message(message.channel, "{} this command requires an option!".format(message.author.mention))
            return
        elif option == "harambe":
            await send_file(message, "assets/pics/harambe/harambe-dead.jpg")
        elif message.mentions[0] == client.user:
            await client.send_message(message.channel, 'The bullet ricocheted off of {} and {} shot themself!'.format(client.user.mention, message.author.mention))
            await send_file(message, "assets/pics/misc/rip.gif")
        elif message.author == message.mentions[0]:
            await client.send_message(message.channel, '{} shot themself!'.format(message.author.mention))
            await send_file(message, "assets/pics/misc/rip.gif")
        else:
            await client.send_message(message.channel, '{} shot {}!'.format(message.author.mention, message.mentions[0].mention))
            await send_file(message, "assets/pics/misc/gunshot.gif")
        return
    if base == 'hug':
        if option == None:
            await client.send_message(message.channel, "{} this command requires an option!".format(message.author.mention))
            return
        elif message.author == message.mentions[0]:
            await send_file(message, "assets/pics/misc/foreveralone.jpg")
        elif message.mentions[0] == client.user:
            await client.send_message(message.channel, '{} hugged {}!'.format(message.author.mention, client.user.mention))
            await send_file(message, "assets/pics/misc/hugShenbot.png")
        else:
            await client.send_message(message.channel, '{} hugged {}!'.format(message.author.mention, message.mentions[0].mention))
            await send_file(message, "assets/pics/misc/hug.gif")
    if base == 'hack':
        if option == None:
            await client.send_message(message.channel, "{} this command requires an option!".format(message.author.mention))
            return
        elif message.author == message.mentions[0]:
            await client.send_message(message.channel, '{} hacked themself!'.format(message.author.mention, client.user.mention))
            await send_file(message, "assets/pics/misc/failedHack.jpg")
        elif message.mentions[0] == client.user:
            await client.send_message(message.channel, '{} tried to hack {} and failed miserably!'.format(message.author.mention, client.user.mention))
            await send_file(message, "assets/pics/misc/failedHack.jpg")
        else:
            await client.send_message(message.channel, '{} hacked {}!'.format(message.author.mention, message.mentions[0].mention))
            await send_file(message, "assets/pics/misc/hacked.jpg")

if __name__ == "__main__":
    client.run(login['email'], login['password'])
