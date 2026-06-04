import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 7156099919

MSG_EFFECT = 5046509860389126442

SHORT_URL = "https://vplink.in" # shortner url 
SHORT_API = "4a98bc00521b68207331e70bd5ebe380e8a855e8" # shortner API
SHORT_TUT = "https://t.me/Tutorialfyy" # shortner tutorial link

# Bot Configuration
SESSION = "BotifyX-Botz"
TOKEN = "8935186029:AAFkOH3RQXwcuNGQUD4gpOE8RN4cXpzKcJA" # Bot token
API_ID = "31761013" # API ID
API_HASH = "3d55d62014467b2a922c6c0d6d95deae" # API HASH
WORKERS = 5

DB_URI = "" # MongoDB URI
DB_NAME = "BotifyX-Filestore"

FSUBS = [[-1003483476894, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL =  -1003891531589  # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [7537243058]
# Bot Settings
DISABLE_BTN = True
PROTECT = False # For content protection stops message forwarding and copying from the bot and same goes for the screenshot

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!! {mention}× sᴇɴᴘᴀɪ 🎊\n</b><blockquote><b>ʟᴏᴠᴇ ᴄᴏʀɴ & ᴊᴀᴠ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ..</b></blockquote>\n<blockquote>››ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/BLURPLEOG'>彡 ᗷᒪᑌᖇᑭᒪᗴᗝᘜ 彡</a></blockquote>",
    "FSUB": "<blockquote>›› ʜᴇʏ {mention}× sᴇɴᴘᴀɪ 🎊</blockquote>\n<blockquote><b>ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b></blockquote>",\n<blockquote>››ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/BLURPLEOG'>彡 ᗷᒪᑌᖇᑭᒪᗴᗝᘜ 彡</a></blockquote>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: <a href='https://t.me/LustyDormNeT'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>\n<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/HypoFlix_Network'>ʜʏᴘᴏғʟɪx ɴᴇᴛᴡᴏʀᴋ</a> \n›› ᴏᴡɴᴇʀ: @BlurpleOg\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @BlurpleOg</b></blockquote>",
    "CHANNELS":"<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Scope'>ᴏᴛᴀᴋᴜ_ɴᴀᴛɪᴏɴx</a>\n<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/Moviess_SpOT'>ᴀɴɪ_ᴍᴏᴠɪᴇ's ᴍᴀɴɪᴀ</a>\n›› ᴀɴɪᴍᴇ ᴇᴅɪᴛᴢ: <a href='https://t.me/Blurpleog'>ᴀɴɪᴍᴇ'ᴢ ᴇᴅɪᴛ'ᴢ</a>\n›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/LustyDormNeT'>𝖫𝗎𝗌𝗍𝗒 𝖣𝗈𝗋𝗆 𝖭𝖾𝗍</a>\n›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/PornhwaRange'>ᴘᴏʀɴʜᴡᴀ ғʟɪx</a>\n›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/HypoFlix_Network'>ᴏᴛᴀᴋᴜғʟɪx</a>\n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @BlurpleOg</b></blockquote>",
    "REPLY": "<b>ғᴜᴄᴋ ᴏғғ ʙɪᴛᴄʜ !!!</b>",
    "SHORT_MSG": "<blockquote><b>✧ TOKEN EXPIRED</b></blockquote>\n<blockquote>›› ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴛᴏ ʀᴇɢᴀɪɴ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ғɪʟᴇs\n›› ᴠᴀʟɪᴅ ᴄʀᴇᴅɪᴛs: 5 ᴄʀᴇᴅɪᴛs</blockquote>\n────────────────────────\n<blockquote>›› ᴡʜᴀᴛ ɪs ᴀ ᴛᴏᴋᴇɴ?</blockquote>\n<blockquote>≡  ᴇᴀᴄʜ ᴀᴅ ʙʏᴘᴀss ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ 5 ᴄʀᴇᴅɪᴛs.ᴏɴᴇ ᴄʀᴇᴅɪᴛ ɪs ᴄᴏɴsᴜᴍᴇᴅ ᴘᴇʀ ғɪʟᴇ/ʟɪɴᴋ ᴀᴄᴄᴇss.</blockquote>",
    "START_PHOTO": "https://ibb.co/R47nC0JZ",
    "FSUB_PHOTO": "https://ibb.co/3mCfKSdt",
    "SHORT_PIC": "https://ibb.co/yFXMPyyj",
    "SHORT": "https://ibb.co/LzVSRZc6",
    "SHORT_VERIFY": "https://ibb.co/0yLCY4Fd",
    "PREMIUM_PLANS_PIC": "https://ibb.co/R47nC0JZ",
    "QR_PAYMENT_PIC": "https://ibb.co/rKXrj6yB"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
