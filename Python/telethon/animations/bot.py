# -*- coding: utf-8 -*-
import asyncio

from telethon import TelegramClient, events
from trashguy import TrashGuy

from utils import *

api_id = 'INSERT API ID HERE'
api_hash = 'INSERT API HASH HERE'

client = TelegramClient('polar', api_id, api_hash)

# Trash Dance
@client.on(events.NewMessage(outgoing=True, pattern='!d .*'))
async def trash_dance(event):
    m = await event.respond('dance')

    dance_msg = (event.message.message).split('!d ')

    animation = TrashGuy(dance_msg[1])

    await asyncio.sleep(2)
    for frame in animation:
        await client.edit_message(m, frame)

# Rabbit 
@client.on(events.NewMessage(pattern='!b.*'))
async def rabbit_message(event):
    msg = (event.message.message).split('!b ')
    await event.delete()
    if len(msg) == 1:
        await event.respond(create_rabbit())
    else:
        m = await event.respond(create_rabbit(''))
        text = ''

        for char in msg[1]:
            text += char
            #await asyncio.sleep(0.5)
            await client.edit_message(m, create_rabbit(text))

    
client.start()
client.run_until_disconnected()

