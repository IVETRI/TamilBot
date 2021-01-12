# Tamil UserBot 

```
#include <std/disclaimer.h>
/**
 1) இந்த போட்டின் எந்தவொரு முறையற்ற பயன்பாட்டிற்கும் நான் பொறுப்பல்ல...
 2) இந்த போட் மீம்ஸுடன் வேடிக்கை பார்க்கும் நோக்கத்திற்காக வடிவமைக்கப்பட்டுள்ளது,
அத்துடன் திறமையாக குழுக்களை நிர்வகித்தல்.
/**
```

[![tamilbot logo](https://telegra.ph/file/2790938cacb9aa80d478c.jpg)](https://heroku.com/deploy?template=https://github.com/ivetri/tamilbot)

## Support
Join [TeleBot Support group](https://t.me/TamilSupport) for updates and new plugin suggestions.
Do fork and star the repo 

### Session String 

<a href="https://generatestringsession.ivetri.repl.run/" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>

<a href="https://repl.it/@ImSaravanakrish/Tamilbot" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>

## Deploy TamilBot to Heroku:

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fivetri%2Ftamilbot%2Ftree%2Fbugs&template=https%3A%2F%2Fgithub.com%2Fivetri%2Ftamilbot)
<p align="center">
  <a href="https://github.com/ivetri/tamilbot/fork">
    <img src="https://img.shields.io/github/forks/ivetri/tamilbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/ivetri/tamilbot">
    <img src="https://img.shields.io/github/stars/ivetri/tamilbot?style=social">
  </a>
</p>


## நான் அதை எவ்வாறு பயன்படுத்துவது?

தமிழ் பாட்-யை உள்ளமைக்க, எங்கள் [TamilUserBot](https://t.me/TamilUserBot) ஐப் பார்க்கலாம்.
தயவுசெய்து, எங்கள் குழுக்களில் எங்களிடம் கேட்பதற்கு முன்,
நீங்கள் சேனல் மற்றும் தேவையான அனைத்து படிகளையும் பின்பற்றியுள்ளீர்கள் என்பதை உறுதிப்படுத்திக் கொள்ளுங்கள்.
[Support group](https://t.me/Tamilsupport)

## குழுக்கள் மற்றும் ஆதரவு:

புதிய அம்சங்கள் அல்லது அறிவிப்புகளைப் பற்றி நீங்கள் தெரிந்து கொள்ள விரும்பினால், நீங்கள் எங்கள் [சேனலில்](https://t.me/TamilUserBOT) சேரலாம்.

கலந்துரையாடல், பிழை அறிக்கையிடல் மற்றும் உதவிக்கு, நீங்கள் [எங்கள் கலந்துரையாடல் குழுவில்](https://t.me/TamilSupport) சேரலாம்.

நீங்கள் ஒரு பிழையைக் கண்டால், அதை எங்கள் டெலிகிராம் குழுவில் புகாரளிக்க பயப்பட வேண்டாம் அல்லது இந்த களஞ்சியத்தில் சிக்கலைத் திறக்கவும். அதிகாரப்பூர்வமற்றது
[This Repo](https://github.com/IVETRI/TamilBot) இல் காணப்படும் எங்கள் மைய களஞ்சியத்தை பாதிக்கும் சிக்கல்களுக்கு மட்டுமே நாங்கள் உதவுவோம்.

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
