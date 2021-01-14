"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname

from userbot import ALIVE_NAME, CMD_HELP, StartTime, tamildef, tamilversion

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
TAMIL_IMG = Config.ALIVE_PIC
TAMIL = (
    str(Config.CUSTOM_ALIVE_TEXT)
    if Config.CUSTOM_ALIVE_TEXT
    else "☬ MY BOT IS RUNNING SUCCESFULLY ☬"
)
EMOJI = str(Config.CUSTOM_ALIVE_EMOJI) if Config.CUSTOM_ALIVE_EMOJI else "✨"


@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    uptime = await catdef.get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    hmm = bot.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if TAMIL_IMG:
        tamil_caption = f"**{TAMILCAT}**\n\n"
        tamil_caption += f"**{EMOJI} My Master:** ✨[{DEFAULTUSER}](tg://user?id={hmm})✨\n"
        tamil_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        tamil_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        tamil_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
        tamil_caption += f"**{EMOJI} tamiluserbot Version :** `{tamilversion}`\n"
        tamil_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n\n"
        tamil_caption += "   **[TAMIL USERBOT]**(https://github.com/ivetri/tamilbot) "
        await borg.send_file(
            alive.chat_id,
            TAMIL_IMG,
            caption=cat_caption,
            reply_to=reply_to_id,
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{TAMILCAT}**\n\n"
            f"**{EMOJI} My Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} tamiluserbot Version :** `{tamilversion}`\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n\n"
            "   **[TAMIL USERBOT]**(https://github.com/ivetri/tamilbot) ",
        )


@borg.on(admin_cmd(outgoing=True, pattern="(ialive|live)$"))
@borg.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    hmm = bot.uid
    tamil_caption = f"**Catuserbot is Up and Running**\n"
    tamil_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    tamil_caption += f"**  -tamiluserbot Version :** `{tamilversion}`\n"
    tamil_caption += f"**  -Python Version :** `{python_version()}\n`"
    tamil_caption += f"**  -My peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def _(event):
    try:
        await event.delete()
    except BaseException:
        pass
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.cat()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await bot.send_file(event.chat_id, open("temp.webp", "rb"), reply_to=reply_to_id)


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Var.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n**Syntax : **`.alive`\
      \n**Usage : ** status of bot.\
      \n\n**Syntax : **`.ialive` or `.live`\
      \n**Usage : ** inline alive.\
      \n\n**Synatx :** `.cat`\
      \n**Usage : **Random tamil stickers"
    }
)
