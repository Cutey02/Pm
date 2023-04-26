from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/080436e7e221f2ae601e8.jpg",
        caption=f"""💫ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴏᴡɴᴇʀ💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨𝙆𝙄𝙉𝙂 𝙊𝙁 𝙈𝙐𝙎𝙄𝘾✨", url=f"https://t.me/Gplove_Rp")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/080436e7e221f2ae601e8.jpg",
        caption=f"""💫ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴏᴡɴᴇʀ💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨𝙆𝙄𝙉𝙂 𝙊𝙁 𝙈𝙐𝙎𝙄𝘾✨", url=f"https://t.me/Gplove_Rp")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("mukku")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f1ac29224978252c13cba.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫support Group💫", url=f"https://t.me/+ToqLdbxeg7o2MGI9")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("kittu")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f1ac29224978252c13cba.jpg",
        caption=f"""🦋•────────────────•🦋 \n          🇸𝗧𝗨𝗗𝗬  𝙉𝘿 𝘾𝙍𝙔😭
🦋•────────────────•🦋
┏━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━┓

𝐌𝗢𝐇𝗔𝐁𝗕𝐀𝗧 𝐇𝗢 𝐆𝗔𝐘𝗜 𝐓𝗛𝐈 𝐃𝗢𝐍𝗢 𝐊𝗢[ Sᴛᴜᴅʏ ɴᴅ ᴍᴇ ] 𝐄𝗞 𝐀𝗥S𝗔 𝐇𝗢 𝐆𝗬𝐀
👉👈 𝐌𝗘𝐑𝗔 𝐘𝗘 𝐈𝗦𝐇𝗤 𝐓𝗛𝐀 𝐃𝗢 𝐓𝗔𝐑𝗙𝐀 𝐄𝗞 𝐓𝗔𝐑𝗙𝐀 𝐇𝗢 𝐆𝗔𝐘𝗔❤️😭🦋😂

┗━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━┛""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫support Group💫", url=f"https://t.me/+ToqLdbxeg7o2MGI9")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/080436e7e221f2ae601e8.jpg",
        caption=f"""💫ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨sᴏᴜʀᴄᴇ✨", video=f"https://telegra.ph/file/bdb469a86fb4e18ab9930.mp4")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/080436e7e221f2ae601e8.jpg",
        caption=f"""💫ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨sᴏᴜʀᴄᴇ✨", video=f"https://telegra.ph/file/bdb469a86fb4e18ab9930.mp4")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/080436e7e221f2ae601e8.jpg",
        caption=f"""💫ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ💫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨sᴏᴜʀᴄᴇ✨", video=f"https://telegra.ph/file/bdb469a86fb4e18ab9930.mp4")
                ]
            ]
        ),
    )

