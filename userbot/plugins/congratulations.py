from telethon import events
import random, re
from uniborg.util import admin_cmd

RUNSREACTS = [
    "`வாழ்த்துக்கள் நண்பா!`",
    "`உன்னை நினைத்து பெருமை படுகிறேன்!`",
    "`இது கொண்டாடப்பட வேண்டும்! வாழ்த்துக்கள்!`",
    "`உங்கள் தகுதியான வெற்றிக்கு வாழ்த்துக்கள்.`",
    "`உங்களுக்கு மனமார்ந்த வாழ்த்துக்கள்.`",
    "`உங்கள் சாதனைக்கு வாழ்த்துக்கள்.`",
    "`வாழ்த்துக்கள்! மற்றும் உங்கள் அடுத்த சாகசத்திற்கும் வாழ்த்துக்கள்!”`",
    "`நீங்கள் பெரிய காரியங்களைச் செய்வதைக் கண்டு மகிழ்ச்சி அடைகிறேன்.`",
    "`இன்று உங்களுக்கு மிகவும் மகிழ்ச்சியாக இருக்கிறது. என்ன ஒரு அற்புதமான சாதனை!`",
]

@borg.on(admin_cmd(pattern="congo"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)
