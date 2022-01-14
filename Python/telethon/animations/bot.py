# -*- coding: utf-8 -*-
import asyncio

from telethon import TelegramClient, events

from utils import *

api_id = 'INSERT API ID HERE'
api_hash = 'INSERT API HASH HERE'

client = TelegramClient('client', api_id, api_hash)

@client.on(events.NewMessage(pattern='!b.*'))
async def cueio(event):
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

