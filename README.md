# PySelf Telegram Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Commands](#commands)
   - [Help](#help)
   - [Ping](#ping)
   - [Info](#info)
   - [Block](#block)
   - [Time, Photo, Action, Status](#profile-settings)
   - [Set Photo](#set-photo)
   - [Set Font](#set-font)
   - [Set Name](#set-name)
   - [Set Bio](#set-bio)
   - [Save](#save)
   - [Join](#join)
   - [Leave](#leave)
   - [Download](#download)
3. [Profile Updater](#profile-updater)
4. [Dependencies](#dependencies)
5. [How to Run](#how-to-run)
6. [Contact](#contact)

## Introduction<a name="introduction"></a>

`pyself` is a Telegram bot written in Python using the Pyrogram library. This bot provides various features to manage your Telegram profile, interact with users, and perform actions at scheduled intervals.

## Commands<a name="commands"></a>

### Help<a name="help"></a>

Use the command `.help` to get a list of available commands.

Example:
```
.help
```

### Ping<a name="ping"></a>

Check the bot's online status and server usage.

Example:
```
.ping
```

### Info<a name="info"></a>

Retrieve information about a user by replying to their message.

Example:
```
.info
```

### Block<a name="block"></a>

Block the user in a private chat.

Example:
```
.block
```

### Profile Settings<a name="profile-settings"></a>

Toggle various profile settings on or off.

Example:
```
.time on
.photo off
.action on
.status off
```

### Set Photo<a name="set-photo"></a>

Set your profile photo by replying to a message containing a photo.

Example:
```
.setphoto
```

### Set Font<a name="set-font"></a>

Set the font used for profile information.

Example:
```
.setfont
```

### Set Name<a name="set-name"></a>

Set your first name by replying to a message with your desired name.

Example:
```
.setname
```

### Set Bio<a name="set-bio"></a>

Set your bio by replying to a message with your desired bio.

Example:
```
.setbio
```

### Save<a name="save"></a>

Save a message by replying to it.

Example:
```
.save
```

### Join<a name="join"></a>

Join a group or channel by replying to an invite link.

Example:
```
.join
```

### Leave<a name="leave"></a>

Leave the current group or channel.

Example:
```
.leave
```

### Download<a name="download"></a>

Download media (photo or video) by replying to the message containing it.

Example:
```
.d
```

## Profile Updater<a name="profile-updater"></a>

The bot includes a profile updater that runs periodically to update profile information.

## Dependencies<a name="dependencies"></a>

- Pyrogram
- Aiocron
- Psutil

## How to Run<a name="how-to-run"></a>
1. Clone the project:
```bash
git clone https://github.com/AFzOfficial/pyself.git
cd pyself
```
3. Setup env:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Configure your bot by editing the `config.ini` file.
```bash
cp config.ini.example config.ini
```
5. Run the bot:
```bash
# start a tmux session for keep bot running
tmux

python3 main.py
```

## Contact<a name="contact"></a>

For any issues or inquiries, please contact the developer:

- Telegram: [AFz](https://t.me/TalkToHand)
