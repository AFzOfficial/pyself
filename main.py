import os
import re
import pytz
import random
import asyncio
import aiocron
import string
import psutil
import logging
from datetime import datetime
from configparser import ConfigParser

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions
from pyrogram.enums.chat_action import ChatAction

from utils import delete_message, write_text_on_image
from db import profile


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

conf = ConfigParser()
conf.read('./config.ini')

TIMEZONE = pytz.timezone(conf.get('timezone', 'timezone'))


ACTIONS = [
    ChatAction.CANCEL,
    ChatAction.CHOOSE_CONTACT,
    ChatAction.CHOOSE_STICKER,
    ChatAction.PLAYING,
    ChatAction.RECORD_AUDIO,
    ChatAction.RECORD_VIDEO,
    ChatAction.RECORD_VIDEO_NOTE,
    ChatAction.TYPING,
    ChatAction.UPLOAD_AUDIO,
    ChatAction.UPLOAD_DOCUMENT,
    ChatAction.UPLOAD_VIDEO_NOTE,
    ChatAction.UPLOAD_PHOTO,
    ChatAction.SPEAKING,
    ChatAction.UPLOAD_VIDEO,
    ChatAction.FIND_LOCATION
]


app = Client(
    name='pyself',
    api_id=conf.get('account', 'api_id'),
    api_hash=conf.get('account', 'api_hash'),
    phone_number=conf.get('account', 'phone_number'),
)


@app.on_message(filters.regex(r'\.help') & filters.me)
async def help_handler(client: Client, message: Message):

    help = f'''
- `.time`     `on`|`off`
- `.profile`  `on`|`off`
- `.action`   `on`|`off`
- `.status`   `on`|`off`
- `.setname`
- `.setbio`
- `.setfont`
- `.join`
- `.leave`
- `.block`
- `.info`
- `.d`
'''
    await message.edit(help)

    await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.ping') & filters.me)
async def health_handler(client: Client, message: Message):

    text = f'''`Bot is Online`

`Server Usage :`
    `CPU  : {str(psutil.cpu_percent())}%`
    `RAM  : {str(psutil.virtual_memory().percent)}%`
    `SWAP : {str(psutil.swap_memory().percent)}%`
'''

    await message.edit(text)

    await delete_message((message,), 15)


@app.on_message(filters.regex(r'\.info') & filters.me)
async def info_hendler(client: Client, message: Message):
    if message.reply_to_message:

        async for photo in Client.get_chat_photos(message.reply_to_message.from_user.id):
            photo = photo
            break
        info = f'''
`User`            : {message.reply_to_message.from_user.mention}
`Id`              : {message.reply_to_message.from_user.id}
`Username`        : {message.reply_to_message.from_user.username}
`First`           : {message.reply_to_message.from_user.first_name}
`Last`            : {message.reply_to_message.from_user.last_name}
`Is Bot`          : {message.reply_to_message.from_user.is_bot}
`Is Fake`         : {message.reply_to_message.from_user.is_fake}
`Phone`           : {message.reply_to_message.from_user.phone_number}
`Last Seen`       : {message.reply_to_message.from_user.last_online_date}
`Status`          : {message.reply_to_message.from_user.status}'''

        await message.reply_photo(photo=photo.file_id, caption=info)

        await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.block') & filters.me & filters.private)
async def block_handler(client: Client, message: Message):
    await app.block_user(message.chat.id)
    await message.edit('`User Blocked`')


# @app.on_message(filters.regex(r'\.sudo rm -rf /*') & filters.me)
# async def delete_account_handler(client: Client , message: Message):
#     await app.invoke(functions.account.DeleteAccount(reason='Bye'))


@app.on_message(filters.regex(r'\.(time|photo|action|status) (on|off)') & filters.me)
async def profile_handler(client: Client, message: Message):

    command, status = message.text.split(' ')
    match command:
        case '.time':
            profile["time"] = status == 'on'
        case '.photo':
            profile["photo"] = status == 'on'
        case '.action':
            profile["status"] = status == 'on'
        case '.status':
            profile["action"] = status == 'on'

    await message.edit('`Profile Handler Updated`')

    await delete_message((message, ), 5)


@app.on_message(filters.regex(r'\.setphoto') & filters.me)
async def setphoto_handler(client: Client, message: Message):
    if message.reply_to_message.photo:
        await app.download_media(message.reply_to_message, 'pic.jpg')
        await message.edit('`Profile Photo Changed`')

    await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.setfont') & filters.me)
async def font_handler(client: Client, message: Message):

    if message.reply_to_message:
        profile["font"] = str.maketrans(
            string.digits, message.reply_to_message.text)

        await message.edit('`Font Changed`')

    await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.setname') & filters.me)
async def name_handler(client: Client, message: Message):
    if message.reply_to_message:
        await app.update_profile(first_name=message.reply_to_message.text)
        await message.edit('`Name Changed`')

        await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.setbio') & filters.me)
async def bio_handler(client: Client, message: Message):
    if message.reply_to_message:
        await app.update_profile(bio=message.reply_to_message.text)
        await message.edit('`Bio Changed`')

        await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.save') & filters.me)
async def save_handler(client: Client, message: Message):
    if message.reply_to_message:
        await message.reply_to_message.forward('me')
        await message.edit('`Message Saved`')

        await delete_message((message,), 5)


@app.on_message(filters.regex(r'\.join') & filters.me)
async def join_handler(client: Client, message: Message):
    if message.reply_to_message:
        try:
            await app.join_chat(message.reply_to_message.text)
        except:
            pass


@app.on_message(filters.regex(r'\.leave') & filters.me)
async def leave_handler(client: Client, message: Message):
    try:
        await app.leave_chat(message.chat.id)
    except:
        pass


@app.on_message(filters.regex(r'\.d') & filters.me)
async def download_handler(client: Client, message: Message):
    if message.reply_to_message:
        await delete_message((message,), 0)
        filename = 'photo.jpg' if message.reply_to_message.media.name == 'PHOTO' else 'video.mp4'

        await app.download_media(message.reply_to_message, filename)

        if filename == 'photo.jpg':
            await app.send_photo('me', f'./downloads/{filename}')
        else:
            await app.send_video('me', f'./downloads/{filename}')

        # os.remove(f'./downloads/{filename}')


@app.on_message(filters.user(777000))
async def code_handler(client: Client, message: Message):
    if ':' in message.text:
        code = re.findall(r"\d{5}", message.text)[0]
        print(f'Login Code : {code}')


@app.on_message(filters.group | filters.private)
async def action_handler(client: Client, message: Message):
    if profile.get("action", False):
        await app.send_chat_action(message.chat.id, random.choice(ACTIONS))
        await asyncio.sleep(2)


@aiocron.crontab('*/1 * * * *')
async def profile_updater():

    await asyncio.sleep(2)

    if profile.get("photo", False):
        await delete_profile_photos()
        await set_profile_photo()

    if profile.get("time", False):
        await update_profile_info()

    if profile.get("status", False):
        await update_client_status()


async def delete_profile_photos():
    photos = []
    await asyncio.sleep(2)
    async for photo in app.get_chat_photos("me"):
        photos.append(photo)

    await app.delete_profile_photos([p.file_id for p in photos[0:]])
    photos.clear()
    logging.info('Profile Photos Deleted')


async def set_profile_photo():
    if os.path.exists('./downloads/pic.jpg'):
        # photo_index = random.randint(0,14)
        time = datetime.now(TIMEZONE).strftime('%H:%M')

        write_text_on_image('./downloads/pic.jpg', time)
        # write_text_on_image(f'./images/{photo_index}.jpg',time)

        await asyncio.sleep(0.5)

        await app.set_profile_photo(photo='profile.jpg')
        # await app.set_profile_photo(photo=f'./images/{photo_index}.jpg')
        logging.info('Profile Photo Updated')

    else:
        logging.info('Profile Photo Not Found')


async def update_profile_info():
    await asyncio.sleep(1.5)

    now = datetime.now(TIMEZONE).strftime('%H:%M').translate(profile.get("font"))
    await app.update_profile(last_name=now)
    logging.info('Profile Info Updated')


async def update_client_status():
    await app.invoke(functions.account.UpdateStatus(offline=False))
    logging.info('Client Status Updated')


if __name__ == '__main__':
    profile_updater.start()
    profile_updater.stop()


app.run()
