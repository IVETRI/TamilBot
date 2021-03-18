from math import ceil
import asyncio
import json
import random
import re
import io
import os
import urllib
from re import findall
import requests
from telethon import Button, custom, events, functions
from userbot import ALIVE_NAME, CMD_LIST

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/2790938cacb9aa80d478c.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


USER_BOT_WARN_ZERO = "`I had warned you not to spam. Now you have been blocked and reported until further notice.`\n\n**GoodBye!** "

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Tamilbot"

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Bot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© TamilBot Help",
                text="{}\n🔘ℓσα∂є∂ ρℓυgιηѕ: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Showing Stats For {DEFAULTUSER}'s TamilBot** \nNote --> Only Owner Can Check This \n(C) @tamilsupport",
                buttons=[
                    [custom.Button.inline("Show Stats ?", data="terminator")],
                    [Button.url("Repo 🇮🇳", "https://github.com/ivetri/tamilbot")],
                    [Button.url("Join Channel ❤️", "t.me/Tamilsupport")],
                ],
            )
            await event.answer([result])
        elif event.query.user_id == bot.uid and query.startswith("**Hello"):
            result = builder.photo(
                file=WARN_PIC,
                text=query,
                buttons=[
                        [
                            custom.Button.inline("Request ", data="askme"),
                            custom.Button.inline("Chat 💭", data="whattalk"),
                        ],
                        [custom.Button.inline("To spam 🚫", data="dontspamnigga")],
                        [custom.Button.inline("What is this ❓", data="pmclick")],
                    ],
                )
    
            await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_popp_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_popp_up_alert, cache_time=0, alert=True)


    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Userbot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            sedok = "Don’t use mine 😒 get your own @tamiluserbot"
            await event.answer(sedok, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        if plugin_name in CMD_LIST:
            help_string = f"**💫 PLUGIN NAME 💫 :** `{plugin_name}` \n{CMD_LIST[plugin_name]}"
        reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n\n**(C) @TamilSupport** ".format(plugin_name)
        if len(reply_pop_up_alert) >= 4096:
            crackexy = "`Pasting Your Help Menu.`"
            await event.answer(crackexy, cache_time=0, alert=True)
            out_file = reply_pop_up_alert
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f"Pasted {plugin_name} to {url}",
                link_preview=False,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )
        else:
            await event.edit(
                message=reply_pop_up_alert,
                buttons=[[custom.Button.inline("Go Back", data="backme")]],
            )


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            text = inlinestats
            await event.answer(text, alert=True)
        else:
            txt = "You Can't View My Masters Stats"
            await event.answer(txt, alert=True)
        

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dontspamnigga")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("You Have Chosed A Probhited Option. Therefore, You Have Been Blocked By TamilBot. 🇮🇳")
        await borg(functions.contacts.BlockRequest(event.query.user_id))
        Poipoi = f"Hello{DEFAULTUSER}, A Noob [Nibba](tg://user?id={him_id}) Selected Probhited Option, Therefore Blocked."
        await tgbot.send_message(LOG_CHAT, poipoi)
   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme")))
    async def sed(event):
        if event.query.user_id != bot.uid:
            sedok = "Don’t use mine 😒 get your own @tamiluserbot"
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.answer("Back", cache_time=0, alert=False)
        # This Is Copy of Above Code. (C) @SpEcHiDe
        buttons = paginate_help(0, CMD_LIST, "helpme")
        sed = f"""вσт σƒ {DEFAULTUSER}

        ⚙️•TαɱιʅBσƚ Mҽɳυ•⚙️ 

        🔘ℓσα∂є∂ ρℓυgιηѕ: {len(CMD_LIST)} """
        await event.edit(message=sed, buttons=buttons)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def rip(event):
            if event.query.user_id == bot.uid:
                reply_pop_up_alert = "This ain't for you, master!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            else:
                await event.edit(
                    f"This is the PM Security for {DEFAULTUSER} to keep away spammers and retards.\n\nProtected by [TamilBot](t.me/TamilBotSupport)"
                )


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"whattalk")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
            await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything Stupid. \nThank You For Contacting Me.")
        textz = f"Hello{DEFAULTUSER}, A [New User](tg://user?id={him_id}). Wants To Talk With You."
        await tgbot.send_message(LOG_CHAT, textz)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
    async def rip(event):
        if event.query.user_id == bot.uid:
            sedok = "Master, You Don't Need To Use This."
            await event.answer(sedok, cache_time=0, alert=True)
            return
        await event.get_chat()
        him_id = event.query.user_id
        await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
        enna = f"Hello{DEFAULTUSER}, A [New User](tg://user?id={him_id}). Wants To Ask You Something.",
        await tgbot.send_message(
            LOG_CHAT, 
            enna
        )
        
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("TamilBot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© TamilBot",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False
            )
        await event.answer([result] if result else None)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Get your own userbot, don't use another's\n Ask Here @TamilSupport for learning how to get userbot!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Get your own userbot, don't use another's\n Ask Here @TamilSupport for learning how to get userbot!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = ""
        try:
            for i in CMD_LIST[plugin_name]:
                help_string += i
                help_string += "\n"
        except:
            pass
        if help_string is "":
            reply_pop_up_alert = "{} is useless".format(plugin_name)
        else:
            reply_pop_up_alert = help_string
        reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
            © TamilBot".format(plugin_name)
        try:
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        except:
            with io.BytesIO(str.encode(reply_pop_up_alert)) as out_file:
                out_file.name = "{}.txt".format(plugin_name)
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption=plugin_name
                )


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 3
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format("✨", x),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("⪬ Previous", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("Next ⪭", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
