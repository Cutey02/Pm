from AnonX import app
from pyrogram import filters


@app.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"✨{reply.from_user.first_name}'𝐒 ɪᴅ✨: {reply.from_user.id}\n\n✨ʏᴏᴜʀ ɪᴅ✨: {message.from_user.id}\n\n✨ɢʀᴏᴜᴘ ɪᴅ✨: {message.chat.id}"
        )
    else:
        message.reply(
            f"✨ʏᴏᴜʀ ɪᴅ✨: {message.from_user.id}\n\n✨ɢʀᴏᴜᴘ ɪᴅ✨: {message.chat.id}"
        )
