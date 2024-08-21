from pyrogram import Client, types, filters
from datetime import datetime 
import asyncio
import random

from pyrogram.errors.exceptions.forbidden_403 import Forbidden
from pyrogram.errors import InviteRequestSent, UserNotParticipant

API_ID = ''  #your ID 
API_HASH = ''  #your hash
PHONE = ''  #your number phone

app = Client('PythonPyro', api_id=API_ID, api_hash=API_HASH, phone_number=PHONE)
print(f'App started at {datetime.now()}')

target_channels = ['yourchanel1', 'yourchanel2', 'yourchanel3', 'yourchanel4', 'yourchanel5', 'yourchanel5']

# your messages 
messages = [
    'DOGS or TON?',
    'Like and sub me',
    'Are you idiot?',
    'Drop me your smile',
    'Hello!Are you here?'
]

@app.on_message(filters.chat(target_channels))
async def channels_reply(client, message: types.Message):
    await asyncio.sleep(3.5)
    dm = await app.get_discussion_message(message.chat.id, message.id)

    # Random messages
    reply_message = random.choice(messages)

    try:
        await dm.reply(reply_message)
    except (Forbidden, UserNotParticipant):
        try:
            await app.join_chat(message.chat.id)
            await dm.reply(reply_message)
        except InviteRequestSent:
            print(f"Request to connect {message.chat.title} send")
        except Exception as e:
            print(f"I can't connect: {e}")

try:
    app.run()
except KeyboardInterrupt:
    print(f'App finished at {datetime.now()}')