"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`தந்தி தலைமையகத்துடன் இணைக்கிறது ...`",
            "`அழைப்பு இணைக்கப்பட்டுள்ளது.`",
            "`Telegram: வணக்கம் இது தந்தி தலைமையகம். இது யார்?`",
            "`Me: தயவுசெய்து என்னை Pavel Durov ப்ரோவுடன் இணைக்கவும்.`",
            "`பயனர் அங்கீகரிக்கப்பட்டவர்.`",
            "`அழைக்கிறது Pavel Durov`  `At +916969696969`",
            "`தனியார் அழைப்பு இணைக்கப்பட்டுள்ளது...`",
            "`Me: வணக்கம், தயவுசெய்து இந்த தந்தி கணக்கை தடைசெய்க.`",    
            "`Pavel: இது யார் என்று எனக்குத் தெரியும்?`",
            "`Me: நான்` @iMvEtRi ",
            "`Pavel: OMG!!! நீண்ட நேரம் பார்க்கவில்லை, வாட்ஸ்அப் சகோதரர்...\nஅவர் கணக்கு 24 மணி நேரத்திற்குள் தடுக்கப்படும் என்பதை உறுதிசெய்கிறேன்.`",
            "`Me: நன்றி, பின்னர் சந்திப்போம்.`",
            "`Pavel: தயவுசெய்து நன்றி சொல்ல வேண்டாம், டெலிகிராம் நம்முடையது. நீங்கள் Freeஆகும் போது ஒரு அழைப்பு விடுங்கள்.`",
            "`Me:ஏதேனும் பிரச்சினை / அவசரநிலை இருக்கிறதா????`",
            "`Pavel:ஆம், டெலிகிராமில் ஒரு பிழை இருக்கிறது v69.6.9.\nநான் அதை சரிசெய்ய முடியாது. முடிந்தால், பிழையை சரிசெய்ய உதவுங்கள்.`",
            "`Me: எனது தந்தி கணக்கில் பயன்பாட்டை எனக்கு அனுப்புங்கள், நான் பிழையை சரிசெய்து அனுப்புகிறேன்.`",
            "`Pavel: நிச்சயம். \nTC Bye Bye :)`",
            "`தனிப்பட்ட அழைப்பு துண்டிக்கப்பட்டது.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
