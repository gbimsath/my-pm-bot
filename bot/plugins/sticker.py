import os
from bot import bot
from pyrogram import*
from pyrogram.types import*


@bot.on_message(filters.command("stickerid") & ~filters.forwarded)
async def sticker_id(_, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("Reply to a sticker.")
    if not reply.sticker:
        return await message.reply("Reply to a sticker.")
    await message.reply_text(f"`{reply.sticker.file_id}`")