# rewritten by @saravanakrish

from telethon import events
from datetime import datetime

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, edit_or_reply

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TamilBot🇮🇳"


@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"__**🚴🏻‍♂️🚴🏻‍♂️ Pong!__**\n➥__**Ping Speed**__ {ms}\n➥ __**Bot**__ __**of**__ [{DEFAULTUSER}](tg://user?id={SURID})"
    )

