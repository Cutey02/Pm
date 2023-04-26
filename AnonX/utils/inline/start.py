from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆𝐀𝐃𝐃 𝐌𝐄 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="▫️ʜᴇʟᴘ▫️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="▫️sᴇᴛᴛɪɴɢ▫️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆𝐀𝐃𝐃 𝐌𝐄 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔸ᴏᴡɴᴇʀ🔸", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="▫️ʜᴇʟᴘ▫️", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔹ɢʀᴏᴜᴘ🔹", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="▫️ᴏғғɪᴄᴇ▫️", url=f"https://t.me/+ToqLdbxeg7o2MGI9",
            )
        ],
        [
            InlineKeyboardButton(
                text="▫️sᴏᴜʀᴄᴇ▫️",
                video=f"https://telegra.ph/file/bdb469a86fb4e18ab9930.mp4",
            )
        ],
     ]
    return buttons
