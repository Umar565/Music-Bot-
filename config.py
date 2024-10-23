import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 9972455
API_HASH = "5b1fd83b698e4e6670f3dcb053eecc06"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8113611662:AAE7JrIo_E7iP2JRzaOZDRkvCw8LzmX9yQQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://mainmusicbot:musicbotdatabase@cluster0.hbvhe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = "-1002357764876"

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6928637808

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("mymusic")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-bf3ece1c-80c2-46d1-a64b-5fb01c345685")

UPSTREAM_REPO = "https://github.com/Umar565/Music-Bot-"
UPSTREAM_BRANCH = "main"
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/Moviez_Backupp"
SUPPORT_GROUP = "https://t.me/studyocean1"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = "19d2fe49f79143fa90e75be9c95255db"
SPOTIFY_CLIENT_SECRET = "9e3e42756a8040a89424e7bf3343fa19"


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQCYKucAljp_NIBQNx7OTesmmAPtUFL8uRRqSF8QDzHYOg38KeMU76lTM6JiN0wj61H5ohdJOBPbrBQnizQC1vJin4etovcCoFYVS0xDOwUaypNABr_vWI4icRJL9zdZnl_5vdRoFUxdiRmhQqAQCoUy9eB40eSpc6sfE-Fxpw1EeDBwH3MZr5S8IxaH9rzDnJI01PzjlQ0zmlcReaS8u5J9WC4-Tuax5kMfyPeHqa5PSNtB9q-v8YPFCF-EYuRWEba2yqVl0Inf8xieWWVXHarjF5DajD7s_Jd4Y7vQeG_LYvRrxI_pzbo-F1kZKyj0NoMVhiTCZTskKiwsTrTJuTr4LqyVZwAAAAGc-p9wAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PING_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
