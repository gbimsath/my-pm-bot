

import requests, json
from bot import bot
import time
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import wget
from pyrogram import enums



@bot.on_message(filters.command("wp") & ~filters.forwarded)
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**✍️ Creating Wallpaper ✍️**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**✍️ Creating Wallpaper ✍️**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    await m.edit("🚀ALMOST THERE!🚀")
    f= message.text
    s=f.replace('/wp ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://api.single-developers.software/wallpaper?search={text}")
    photo = wget.download(lol, 'wallpaper.png')
    await m.delete()
    caption = f"""
✍️__**Wallpaper**__  𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇
🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **@gbimsath_bot**
🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {message.from_user.mention} **
🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[• Gavesh Bimsath 🇱🇰 • ™](https://t.me/gbimsath)**
◇───────────────◇️  
"""
    await _.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_PHOTO)
    time.sleep(2)
    await message.reply_photo(photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•••Telegraph Link•••", url=f"{lol}"
                    )
                ]
            ]
          ),
    )

