# Plugin to show the feda you are banned in.
# Kangers keep credits
# By @Surv_ivor

import os

from telethon.errors import ChatAdminRequiredError
from telethon.errors.rpcerrorlist import MessageTooLongError, YouBlockedUserError
from telethon.tl.functions.users import GetFullUserRequest

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

naam = str(ALIVE_NAME)

bots = "@MissRose_bot"

BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", None)
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)


@borg.on(admin_cmd("fstat ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
        getuser = str(replied_user.user.id)
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + getuser)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await borg.forward_messages(event.chat_id, reply)
                else:
                    await borg.send_message(event.chat_id, fedstat.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    if sysarg == "":
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat")
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await borg.forward_messages(event.chat_id, reply)
                else:
                    await borg.send_message(event.chat_id, fedstat.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    if sysarg.startswith("@"):
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await borg.forward_messages(event.chat_id, reply)
                else:
                    await borg.send_message(event.chat_id, fedstat.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
    if sysarg.isdigit():
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/fedstat " + sysarg)
                fedstat = await conv.get_response()
                if "file" in fedstat.text:
                    await fedstat.click(0)
                    reply = await conv.get_response()
                    await borg.forward_messages(event.chat_id, reply)
                else:
                    await borg.send_message(event.chat_id, fedstat.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")


@borg.on(admin_cmd("roseinfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    sysarg = event.pattern_match.group(1)
    if sysarg == "":
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info")
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_bot `and retry!")
    elif "@" in sysarg:
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")
    elif "" in sysarg:
        async with borg.conversation(bots) as conv:
            try:
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message("/info " + sysarg)
                audio = await conv.get_response()
                await borg.send_message(event.chat_id, audio.text)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("**Error:** `unblock` @MissRose_Bot `and try again!")


@borg.on(admin_cmd(pattern=r"plist ?(.*)", outgoing=True))
async def get_users(show):
    await show.delete()
    if not show.text[0].isalpha() and show.text[0] not in ("/", "#", "@", "!"):
        if not show.is_group:
            await show.edit("Are you sure this is a group?")
            return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "id,reason"
        try:
            if not show.pattern_match.group(1):
                async for user in show.client.iter_participants(show.chat_id):
                    if not user.deleted:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
                    else:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
            else:
                searchq = show.pattern_match.group(1)
                async for user in show.client.iter_participants(
                    show.chat_id, search=f"{searchq}"
                ):
                    if not user.deleted:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
                    else:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            await bot.send_message(BOTLOG_CHATID, mentions)
        except MessageTooLongError:
            file = open("userslist.csv", "w+")
            file.write(mentions)
            file.close()
            await show.client.send_file(
                BOTLOG_CHATID,
                "userslist.csv",
                caption="Group Members in {}".format(title),
                reply_to=show.id,
            )


@borg.on(admin_cmd(pattern=r"blist ?(.*)", outgoing=True))
async def get_users(show):
    await show.delete()
    if not show.text[0].isalpha() and show.text[0] not in ("/", "#", "@", "!"):
        if not show.is_group:
            await show.edit("Are you sure this is a group?")
            return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "id,reason"
        try:
            if not show.pattern_match.group(1):
                async for user in show.client.iter_participants(show.chat_id):
                    if not user.deleted:
                        mentions += f"\n{user.id},⚠️Suspicious/Btc Scammer/Fraudulent activities #Massban🛑"
                    else:
                        mentions += f"\n{user.id},⚠️Suspicious/Btc Scammer/Fraudulent activities #Massban🛑"
            else:
                searchq = show.pattern_match.group(1)
                async for user in show.client.iter_participants(
                    show.chat_id, search=f"{searchq}"
                ):
                    if not user.deleted:
                        mentions += f"\n{user.id},⚠️Suspicious/Btc Scammer/Fraudulent activities #Massban🛑"
                    else:
                        mentions += f"\n{user.id},⚠️Suspicious/Btc Scammer/Fraudulent activities #Massban🛑"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            await bot.send_message(BOTLOG_CHATID, mentions)
        except MessageTooLongError:
            file = open("userslist.csv", "w+")
            file.write(mentions)
            file.close()
            await show.client.send_file(
                BOTLOG_CHATID,
                "userslist.csv",
                caption="Group Members in {}".format(title),
                reply_to=show.id,
            )


@borg.on(admin_cmd(pattern="bgban ?(.*)"))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()


@borg.on(admin_cmd(pattern="bungban ?(.*)"))
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason),
        )
    await event.delete()
