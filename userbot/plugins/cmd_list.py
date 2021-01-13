from telethon import events
import subprocess
import asyncio
import time
from userbot.utils import admin_cmd

#@command(pattern="^.cmds", outgoing=True)
@borg.on(admin_cmd(pattern=r"cmds"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**Plugins பட்டியல்:**\n{o}\n\n**TIP:** __நீங்கள் ஒரு கட்டளைகளை அறிய விரும்பினால்plugin, செய்:-__ \n `.help <plugin name>`அடைப்புக்குறிகள் ** < > இல்லாமல்.**\n__All plugins நேரடியாக வேலை செய்யாமல் போகலாம். Visit:__ @TamilSupport __உதவிக்காக.__"
    await event.edit(OUTPUT)
