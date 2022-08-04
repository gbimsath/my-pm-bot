import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

START_IMG = "https://telegra.ph/file/5b7032c04e994f5319e07.jpg"

START_TEXT = """
Hello there {message.from_user.mention}👋
**I am Assistant bot of [Gavesh Bimsath 🇱🇰](https://t.me/gbimsath)**
"""

START_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("❤️\u200d🔥About❤️\u200d🔥", url='https://gbimsath.ml'),
                 InlineKeyboardButton("⭕️Follow⭕️", url='https://instagram.com/gavesh_bimsath')
                ],
                [
                  InlineKeyboardButton("◈━━━━━━━━━━━━━◈", callback_data="stats_callback"),
                ],
                [
                  InlineKeyboardButton("🆘Help and Commands🆘", callback_data='helpmenu'),
                ],
               ]
)

HELP_TEXT = """ Hey there☄️
I have some fun and useful tools
So you can get a help about them🚀 """

HELP_BUTTON = InlineKeyboardMarkup(
               [
                [
                 InlineKeyboardButton("🎨 Logo maker 🎨", callback_data='logomenu'),
                 InlineKeyboardButton("✨Quote✨", callback_data='quotemenu')
                ],
                [
                  InlineKeyboardButton("🎹 Song 🎹", callback_data='songmenu'),
                  InlineKeyboardButton("🔮Sticker🔮", callback_data='stickermenu')
                ],
                [
                  InlineKeyboardButton("📛More Tools📛", callback_data='toolmenu'),
                ],
                [
                  InlineKeyboardButton("🔗Repo🔗", url='https://github.com/gbimsath/Telegram-feedback-bot'),
                ],
                [
                  InlineKeyboardButton("🔙Back", callback_data='startmenu'),
                ],
               ]
)

BOTSTATUS_TEXT = """
**Bᴏᴛ Sᴛᴀᴛᴜꜱ** ```rᴏᴏᴛ : ~ $ bᴀꜱʜ```
Assistant of *gbimsath*
"""

BOTSTATUS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ]]
)

LOGO_TEXT = """
🔰Help for logo make🔰

Available commands
❥ /logo {text} - create simple random logos
❥ /write {text} - write something
❥ /mlogo {text} - create srilankan mask logo
"""
LOGO_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

TOOLS_TEXT = """
🧰Help for More Tools🧰
Here is the additional Tools of this bot.

Available commands
❥ /covid - Get the Covid status of Srilanka

More tools add in future.
"""
TOOLS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

SONG_TEXT = """
🎧Help for Song Download🎧

Available commands
❥ /song {song name} - Download a song simply.
❥ /song {youtube link} - Download song using youtube link.
"""
SONG_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

#-------------sticker--------------#

STICKER_TEXT = """
Help for Sticker 

Available commands
❥ /stickerid - Reply to a sticker to get it's id.

"""
STICKER_BUTTON = InlineKeyboardMarkup([
  [
    InlineKeyboardButton('🔙Back', callback_data='helpmenu' )
  ]
])

#----------sticke----------#

QUOTE_TEXT = """
💬Help for Quote💬

Available commands
❥ /q - Reply to a message to make it quote.
"""
QUOTE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙Back', callback_data='helpmenu')
        ]]
)

SITHIJATD_TEXT = """ Hey☘️,\n you can find Gavesh in these social medias."""

SITHIJATD_BUTTONS = InlineKeyboardMarkup(
              [
                [
                  InlineKeyboardButton('🔵Telegram🔵' , url='https://t.me/gbimsath'),
                ],
                [
                  InlineKeyboardButton('⭕Instagram⭕' , url='https://instagram.com/gavesh_bimsath'),
                ], 
              ]
)
