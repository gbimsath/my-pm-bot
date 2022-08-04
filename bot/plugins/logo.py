import requests, json
from bot import bot
import time
from pyrogram import filters, idle
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import wget
from pyrogram import enums


@bot.on_message(filters.command("logo") & ~filters.forwarded)
async def on_off_antiarab(_, message: Message):
    m = await message.reply_text("**♻ Creating your Logo ♻**......\n\n[░░░░░░░░░░] 00%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇░░░░░░░░] 20%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇░░░░░░] 40%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇░░░░░] 50%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇░░░] 70%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇░░] 80%")
    await m.edit("**♻ Creating your Logo ♻**......\n\n[▇▇▇▇▇▇▇▇▇▇] 100%")
    await m.edit("📤Uploading....")
    await m.edit("📤Uploading.....")
    await m.edit("🚀ALMOST THERE!🚀")
    f= message.text
    s=f.replace('/logo ' ,'')
    text=s.replace(' ', '%20')
    lol = (f"https://single-developers.up.railway.app/logo?name={text}")
    photo = wget.download(lol, 'pythonlogo.png')
    await m.delete()
    caption = f"""
✍️__**Logo**__ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
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