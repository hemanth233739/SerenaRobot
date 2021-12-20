# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SerenaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 4727554  # integer value, dont use ""
    API_HASH = "b3e57f0a9d80d12857f7bdd393d8f9c6"
    TOKEN = "1931887848:AAE84KOxMQFSY_aRp37VZN0iAJGvFD5095M"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 2022280326 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "AASFCYBERKING" 
    SUPPORT_CHAT = "CrowdXStrikeChat"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001362121266
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001362121266
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    ENV = ANYTHING
    BOT_ID = 1931887848
    DATABASE_URL = "postgres://xfbrdtli:k186fYZpU6t-KvXeV_Xyd0lWefV1JreE@fanny.db.elephantsql.com/xfbrdtli"
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "SpamWatchSupport"
    REDIS_URL = "redis://Zaidrobot:Anmol@123@redis-12356.c284.us-east1-2.gce.cloud.redislabs.com:12356/Zaidrobot"
    MONGO_DB_URI = "mongodb+srv://xforce:xforce@cluster0.2glge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    HEROKU_API_KEY = "a7bdab79-e4f1-41b8-9dc4-c143aa5cdcc6"
    # OPTIONAL 
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "zaid"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
