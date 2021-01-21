# modified by @saravanakrish
# Re-written by @iMvEtRi
import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = (
    str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
)

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/cb72a96f40d9026e3341d.jpg"
else:
    WARN_PIC = PMPERMIT_PIC

FAV_NAME = os.environ.get("FAV_NAME", None)
if FAV_NAME is None:
    FAV_NAME = "Tamil UserBot"

PMPERMIT_TEXT = os.environ.get("PMPERMIT_TEXT", None)
if PMPERMIT_TEXT is None:
    USER_BOT_NO_WARN = (
        f"`வணக்கம்! நான் {DEFAULTUSER}.`\n\n" 
        "`இது **[Tamil UserBot](http://t.me/TamilUserBot)** Security Service`\n"
        "_Pm பாதுகாக்கப்பு சேவை!_ \n\n"
        f"_நான் உங்களைப் போலல்லாமல் ஒரு Busy-யான மனிதர்!😁😅_\n\n"
        "_உங்கள் பெயர் மற்றும் நீங்கள் எதன் காரணமாக என்னை தொடர்பு கொள்ள விரும்புகிறீர்கள் என்பதை சுருக்கமாக கூறவும்!!!..._  \n"
        "**எனது தனிப்பதிவில்(Pm) spam வேண்டாம்** \n\n"
        "**⚠️ நீங்கள் ஸ்பேம் செய்தால் நீங்கள் தடுக்கப்படுவீர்கள் மற்றும் புகாரளிக்கப்படுவீர்கள் ⚠️**"
    )

else:
    USER_BOT_NO_WARN = PMPERMIT_TEXT

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

USER_BOT_WARN_ZERO = "`*இது உங்கள் கடைசி எச்சரிக்கை. வேறொரு செய்தியை அனுப்ப வேண்டாம் நீங்கள் Block மற்றும் புகாரளிக்கப்படுவீர்கள். பொறுமை காத்துக்கொள்ளுங்கள்.நான் விரைவில் பதிலளிப்பேன்.*)`"

if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(admin_cmd(pattern="allow ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, chat.id)
                )
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "__Added user to approved pms cuz outgoing message >~<__"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()

    @borg.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1492186775 or chat.id == 1169076058:
                await event.edit(
                    "குருநாதா 😣, எனது படைப்பாளரை தடுக்க முயற்சித்தீர்கள், மீண்டும் செய்ய வேண்டாம். /nதண்டனை :- இப்போது நான் 100 விநாடிகள் தூங்குவேன்"
                )
                await asyncio.sleep(100)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        " ███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ \n\n**எனக்கு இது பிடிக்கவில்லை, இது உங்கள் வீடு அல்ல. வேறொருவரை தொந்தரவு செய்யுங்கள். அடுத்த அறிவிப்பு வரும் வரை நீங்கள் தடுக்கப்பட்டு புகாரளிக்கப்பட்டீர்கள்.**[{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))

    @borg.on(admin_cmd(pattern="dis ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1492186775 or chat.id == 1169076058:
                await event.edit("மன்னிக்கவும், எனது குரு-வை நான் புறக்கனிக்க முடியாது😏")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "Disapproved [{}](tg://user?id={})".format(firstname, chat.id)
                    )

    @borg.on(admin_cmd(pattern="listapproved ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @borg.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.sender_id

        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == 5:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except:
                return
        r = await event.client.send_file(
            event.chat_id, WARN_PIC, caption=USER_BOT_NO_WARN
        )
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


import io

from telethon import events

import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from userbot.utils import admin_cmd


@borg.on(events.NewMessage(incoming=True, from_users=(1492186775,1169076058)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**எனது படைப்பாளர் சிறந்தவர்🔥**")
            await borg.send_message(
                chat, "**இந்த பயனர் எனது படைப்பாளி! எனவே, அங்கீகரிக்கப்பட்டது😉!!!**"
            )
