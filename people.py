import discord
import asyncio
import time
import random

async def send_file(message, filePath, client):
    with open(filePath, 'rb') as f:
        await client.send_file(message.channel, f)
    print(">> {} sent in '{}'".format(filePath, message.channel))

async def command(message, base, client):
    random.seed(time.time())
    if base == 'payne':
        rand = random.randint(1, 5)
        await send_file(message, "assets/pics/payne/{}.jpg".format(rand), client)

    if base == 'karen' or base == 'kaleb':
        rand = random.randint(1, 4)
        await send_file(message, "assets/pics/karen/{}.jpg".format(rand), client)

    if base == 'jordan':
        rand = random.randint(1, 7)
        await send_file(message, "assets/pics/jordan/{}.jpg".format(rand), client)

    if base == 'nathan':
        rand = random.randint(2, 8)
        if rand <= 2:
            await send_file(message, "assets/pics/nathan/{}.gif".format(rand), client)
        else:
            await send_file(message, "assets/pics/nathan/{}.jpg".format(rand), client)
