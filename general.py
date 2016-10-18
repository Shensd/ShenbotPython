import discord
import asyncio
import time
import random
import wallpaper
import inspire
import os

commands = ["Help --------- help plox",
            "Ping --------- Pong!",
            "Shoot -------- Shoot someone",
            "Fredd -------- :^)",
            "FeelsGood ---- Feels good m8",
            "Wtf ---------- Fuckin what",
            "Succ --------- she succ me",
            "Harambe ------ Dead ape",
            "ShootHarambe - Deader ape",
            "Goober ------- Goober looking mother fucker",
            "Lewd --------- Naughty",
            "Hug ---------- Uhm",
            "Payne -------- honey boo boo bear",
            "Ret ---------- [ret]",
            "DiosMio ------ !",
            "Ziggy -------- me_irl",
            "Shaq --------- Seal of approval",
            "Dick --------- jordan isn't gunna like this one",
            "Really ------- rly",
            "Jimmy -------- snap",
            "Pick --------- pick pocket",
            "Bish --------- bish whut",
            "Pure --------- I dont even remember what this one is",
            "Hack --------- Hack someone",
            "Flip --------- Coin flip",
            "Naruto ------- Pure v2",
            "Weed --------- 420",
            "Image -------- Generate a random wallpaper",
            "Inspire ------ Get Inspired"
            "Voteskip ----- Vote to skip the song Aethex is playing, options are 'Yes', 'No', and 'Start'",
            "Person Commands: Payne, Karen, Jordan, Nathan"]

async def send_file(message, filePath, client):
    with open(filePath, 'rb') as f:
        await client.send_file(message.channel, f)
    print(">> {} sent in '{}'".format(filePath, message.channel))

async def command(message, base, client):
    #Text Commands
    if base == 'help':
        msg = "My commands are: \n ```"
        for command in commands:
            msg += command + "\n"
        msg += "Command Usage: $COMMAND OPTION ```"
        await client.send_message(message.author, msg)
        await client.send_message(message.channel, "{} I have PM'd you my commands".format(message.author.mention))

    if base == 'ping':
        random.seed(time.time())
        if random.randint(1, 5) == 3:
            await client.send_message(message.channel, '{} P̟̥̯̳̱̜̺̻̝̘ͯ̃ͣ̈́͆͑͒ͯͥ́o̷̴̡̨̹͖̤͋ͭͩ̒̽̔̈ͮ̾͆ͥ́ñ̡̘͎͖̯͖̬̦̲͖͙̱͇̦ͦ̅̿̃̀͂ͣ͆ͨ̏̉͐̆ͣ̏̽͗͢ͅg̴̸͚̹̻͖͍͙̪͎̹͉̹̖̗̫̟̱͗̋ͥͯ̓ͪͩ̈̋̍́̒́̀ͪ̑ͨ̚̕͜͜!̡͎̰̻̟̘̩͛͗̅ͤͬ̚'.format(message.author.mention))
        else:
            await client.send_message(message.channel, '{} Pong!'.format(message.author.mention))

    if base == 'flip':
        random.seed(time.time())
        await client.send_message(message.channel, 'Flipping a coin...')
        await asyncio.sleep(1)
        if random.randint(1, 2) == 1:
            await client.send_message(message.channel, 'It landed Tails!')
        else:
            await client.send_message(message.channel, 'It landed Heads!')

    #Picture Commands
    if base == 'image':
        wallpaper.new_wallpaper(message.author.name)
        await send_file(message, "assets/pics/wallpaper.jpg", client)
    if base == 'inspire':
        inspire.new_inspire(message.author.name)
        await send_file(message, "assets/pics/wallpapers/temp.jpg", client)

    if base == 'fredd':
        await send_file(message, "assets/pics/misc/fredd.png", client)

    if base == 'feelsgood':
        random.seed(time.time())
        rand = random.randint(1, 14)
        await send_file(message, "assets/pics/feelsgood/{}.png".format(rand), client)

    if base == 'wtf':
        random.seed(time.time())
        rand = random.randint(1, 5)
        if rand > 3:
            await send_file(message, "assets/pics/wtf/{}.gif".format(rand), client)
        else:
            await send_file(message, "assets/pics/wtf/{}.jpg".format(rand), client)

    if base == 'succ':
        random.seed(time.time())
        rand = random.randint(1, 5)
        await send_file(message, "assets/pics/succ/{}.jpg".format(rand), client)

    if base == 'lewd':
        random.seed(time.time())
        rand = random.randint(1, 6)
        await send_file(message, "assets/pics/lewd/{}.jpg".format(rand), client)

    if base == 'harambe':
        await send_file(message, "assets/pics/harambe/harambe.jpg", client)

    if base == 'shootharambe':
        await send_file(message, "assets/pics/harambe/spon.png", client)

    if base == 'goober':
        await send_file(message, "assets/pics/misc/goober.jpg", client)

    if base == 'ret':
        await send_file(message, "assets/pics/misc/ret.jpg", client)

    if base == 'ziggy':
        await send_file(message, "assets/pics/misc/ziggy.jpg", client)

    if base == 'diosmio':
        await send_file(message, "assets/pics/payne/diosMio.jpg", client)

    if base == 'haq' or base == 'shaq':
        await send_file(message, "assets/pics/misc/shaq.jpg", client)

    if base == 'dick':
        await send_file(message, "assets/pics/misc/dick.jpg", client)

    if base == 'really':
        await send_file(message, "assets/pics/misc/really.jpg", client)

    if base == 'jimmy':
        await send_file(message, "assets/pics/misc/jimmy.jpg", client)

    if base == 'pick':
        await send_file(message, "assets/pics/misc/pick.jpg", client)

    if base == 'bish':
        await send_file(message, "assets/pics/misc/bish.jpg", client)

    if base == 'pure':
        await send_file(message, "assets/pics/misc/pure.jpg", client)

    if base == 'naruto':
        await send_file(message, "assets/pics/misc/naruto.jpg", client)

    if base == 'weed':
        await send_file(message, "assets/pics/nathan/weed.jpg", client)
