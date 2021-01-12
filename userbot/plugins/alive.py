"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`வணக்கம்! (●'◡'●) \nஉங்கள் போட் இயங்குகிறது.\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`எனது உரிமையாளர்`: {DEFAULTUSER}\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nProvided by:` @TamilUserBot\n"
                     "`தரவுத்தள நிலை: தரவுத்தளங்கள் சிறப்பாக செயல்படுகின்றன!\n\nஎன்றும் உன்னுடன்,என் எஜமான்!\n`"
                     "[Deploy This TamilBot Now](https://github.com/Ivetri/TamilBot)")

@borg.on(admin_cmd(pattern=r"sudoalive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`பயன்படுத்தியமைக்கு நன்றி!😊 ")
