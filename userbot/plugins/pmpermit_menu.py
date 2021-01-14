# if you change credits, you get anal cancer and get murdered by russians in 3 days.
"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in heroku vars"
PREV_REPLY_MESSAGE = {}


@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if event.is_private:
         
         PM = ("`வணக்கம்! எனது Menu-வை பார்வையிடுகிறார்கள்,`"
               f"{DEFAULTUSER}.\n"
               "*) __நீங்கள் ஏன் இங்கே இருக்கிறீர்கள் என்பதை எனக்குத் தெரியப்படுத்துங்கள்.__\n"
               "__    (Why You Are Here?)__\n"
               "*) **நீங்கள் இங்கே இருப்பதற்கு பின்வரும் காரணங்களில் ஒன்றைத் தேர்வுசெய்க:**\n"
               "__    Choose one of the following reasons why you are here:__\n\n"
               "`1`. என்னுடன் அரட்டை அடிக்க(Chat With Me)\n"
               "`2`. எனது இன்பாக்ஸை Spam செய்ய.\n"

               "`3`. ஏதாவது விசாரிக்க(inquire something)\n"
               "`4`. சில கோரிக்கைகளுக்காக (Request Something)\n")
         ONE = ("__சரி. உங்கள் கோரிக்கை பதிவு செய்யப்பட்டுள்ளது. தனிப்பதிவில் spam வேண்டாம்.விரைவில் பதிலை எதிர்பார்க்கலாம். அவர் உங்களைப் போலல்லாமல் ஒரு Busy-யான மனிதர்😁.__\n\n"
                "**⚠️ நீங்கள் ஸ்பேம் செய்தால் நீங்கள் தடுக்கப்படுவீர்கள் மற்றும் புகாரளிக்கப்படுவீர்கள். ⚠️**\n\n"
                "__பயன்படுத்தவும்__ `/start` __Menu-விற்க்கு செல்ல....__")
         TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**எனக்கு இது பிடிக்கவில்லை, இது உங்கள் வீடு அல்ல. வேறொருவரை தொந்தரவு செய்யுங்கள். அடுத்த அறிவிப்பு வரும் வரை நீங்கள் தடுக்கப்பட்டு புகாரளிக்கப்பட்டீர்கள்.**")
         FOUR = ("__சரி. நான் இதுவரை உங்கள் செய்தியை பார்க்கவில்லை.வழக்கமாக அனைவருக்கும் பதிலளிப்பேன்.ஆனால், உங்களைப் பற்றி எனக்கு தெரியவில்லை..__\n __நான் திரும்பி வந்ததும் உங்களுக்கு பதிலளிக்கிறேன். விரும்பினால், \n ஏற்கனவே நிறைய செய்திகள் உள்ளன😶__\n **உங்களை Block செய்ய வேண்டாம் என்று நினைத்தால், தயவு செய்து நீங்கள் கூற வருவதை சுருக்கமாக கூறவும்.**")
         FIVE = ("`சரி. நீங்கள் கூற வருவதை சுருக்கமாக கூறவும். நான் உங்களுக்கு உதவ விரும்பினால், விரைவில் உங்களுக்கு பதிலளிப்பேன்.`\n**மீண்டும் மீண்டும் கேட்டால் நீங்கள் தடுக்கப்பட்டு புகார் செய்யப்படுவீர்கள்...**")
         LWARN = ("**இது உங்கள் கடைசி எச்சரிக்கை. வேறொரு செய்தியை அனுப்ப வேண்டாம் நீங்கள் Block மற்றும் புகாரளிக்கப்படுவீர்கள். பொறுமை காத்துக்கொள்ளுங்கள்.நான் விரைவில் பதிலளிப்பேன்.**\n__Use__ `/start` __main menu செல்ல.__")
     
        async with borg.conversation(chat) as conv:
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "1":
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "2":
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         

         elif y == "3":
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "4":
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             await borg.send_message(chat, "`நீங்கள் தவறான கட்டளையை உள்ளிட்டுள்ளீர்கள்.Please send /start. நீங்கள் தடுக்கப்பட்டு புகாரளிக்க விரும்பவில்லை என்றால் மீண்டும் அல்லது மற்றொரு செய்தியை அனுப்ப வேண்டாம்.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
