### Tamil UserBot 

#DISCLAIMER :
```
#include
/**
 1) இந்த போட்டின் எந்தவொரு முறையற்ற பயன்பாட்டிற்கும் நான் பொறுப்பல்ல...
 2) இந்த போட் மீம்ஸுடன் வேடிக்கை பார்க்கும் நோக்கத்திற்காக வடிவமைக்கப்பட்டுள்ளது,
அத்துடன் திறமையாக குழுக்களை நிர்வகித்தல்.
 3) உங்கள் செயல்களுக்கு யாரும் பொறுப்பல்ல...
/**
```

[![tamilbot logo](https://telegra.ph/file/2790938cacb9aa80d478c.jpg)](https://heroku.com/deploy?template=https://github.com/ivetri/tamilbot)

## Give your 💙 and support 

Before clicking on deploy to heroku just click on fork and star just below

<p align="center">
  <a href="https://github.com/ivetri/tamilbot/fork">
    <img src="https://img.shields.io/github/forks/ivetri/tamilbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/ivetri/tamilbot">
    <img src="https://img.shields.io/github/stars/ivetri/tamilbot?style=social">
  </a>
</p>


### Video Tutorial

Click the below button to watch the video tutorial on deploying

<a href="https://youtu.be/blah"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/blah"><img src="https://img.shields.io/youtube/views/blah?style=social">
    
###  GET STRING SESSION FROM REPL RUN

 [![Run on Repl.it](https://camo.githubusercontent.com/05149b448485553c6f14f6430a45c12dcc79ed3c/68747470733a2f2f7265706c2e69742f62616467652f6769746875622f6a61727669733231303930342f4a6172766973)](https://generatestringsession.ivetri.repl.run/)

 [![Run on Repl.it](https://camo.githubusercontent.com/05149b448485553c6f14f6430a45c12dcc79ed3c/68747470733a2f2f7265706c2e69742f62616467652f6769746875622f6a61727669733231303930342f4a6172766973)](https://repl.it/@ImSaravanakrish/Tamilbot#main.py)

## Deploy TamilBot to Heroku:

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fivetri%2Ftamilbot%2Ftree%2Fbugs&template=https%3A%2F%2Fgithub.com%2Fivetri%2Ftamilbot)

### குழுக்கள் மற்றும் ஆதரவு:

[![](https://camo.githubusercontent.com/e531cdc1dbdcb78f8ffe767875a6b6d33c43e2e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e2d54656c656772616d2532304368616e6e656c2d7265642e7376673f6c6f676f3d54656c656772616d)](https://t.me/tamiluserbot)

[![](https://camo.githubusercontent.com/7b0a8bb8af0b2466dd1c38a6c1367ddee45ba266/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6f696e2d54656c656772616d25323047726f75702d626c75652e7376673f6c6f676f3d74656c656772616d)](https://t.me/tamilsupport)

## நான் அதை எவ்வாறு பயன்படுத்துவது?

தமிழ் பாட்-யை உள்ளமைக்க, எங்கள் [TamilUserBot](https://t.me/TamilUserBot) ஐப் பார்க்கலாம்.
தயவுசெய்து, எங்கள் குழுக்களில் எங்களிடம் கேட்பதற்கு முன்,
நீங்கள் சேனல் மற்றும் தேவையான அனைத்து படிகளையும் பின்பற்றியுள்ளீர்கள் என்பதை உறுதிப்படுத்திக் கொள்ளுங்கள்.
[Support group](https://t.me/Tamilsupport)

### Speacial Thanks To paperplane For Their Assistant Modules Bases,
### Thanks To Uniborg

# FORK AT YOUR OWN RISK

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/ivetri/TamilBot
cd TamilBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
