import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '25873459'))
    API_HASH = str(getenv('API_HASH', '284b34da96a3a626beada31439cac353'))
    PICS = (environ.get('PICS','https://graph.org/file/3264d2637eda744390199.jpg')).split()
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6047348955:AAEFcb1FyvgRsywhqjIlIJgLeVqt4Lge4Lo'))
    name = str(getenv('name', 'YDStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001657638670'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1053777957").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = "https://delicate-dulsea-mrspidy-5f88fdde"
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Mr_SPIDY'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else (APP_NAME + '.herokuapp.com' if APP_NAME else '')
    APP_URL = "https://delicate-dulsea-mrspidy-5f88fdde.koyeb.app"
    URL = APP_URL.format(FQDN) if ON_HEROKU or NO_PORT else \
        APP_URL.format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://spidy:MongoDB1432@cluster0.khbbz.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'YourDemandZone'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
