# (c) @Mr_SPIDY
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
import random
logger = logging.getLogger(__name__)
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name, Var.OWNER_ID)
from pyrogram.types import ReplyKeyboardMarkup
            
            
@StreamBot.on_message((filters.command("start")) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/a8095ab3c9202607e78ad.jpg",
                caption=f"{m.from_user.mention},\n\n<b><i>⚠️ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ.</i></b>\n\n<i>ᴅᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 😊</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔   ᴜᴘᴅᴀᴛᴇꜱ  ᴄʜᴀɴɴᴇʟ   ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>ꜱᴏᴍᴇᴛʜɪɴɢ  ᴡᴇɴᴛ  ᴡʀᴏɴɢ  <a href='https://telegram.me/Mr_SpidyBot'>ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ꜰᴏʀ  ꜱᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    button = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("Join Update Channel", url="https://t.me/YourDemandZone")
        ]]
    )

    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo=random.choice(Var.PICS),
        caption=f'{m.from_user.mention(style="md")},\n\nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ɢᴇɴᴇʀᴀᴛᴏʀ  ʙᴏᴛ.\n\nᴊᴜꜱᴛ  ꜱᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ꜰɪʟᴇ  ᴀɴᴅ  ɢᴇᴛ  ᴀ  ᴅɪʀᴇᴄᴛ  ᴅᴏᴡɴʟᴏᴀᴅ  ʟɪɴᴋ  ᴀɴᴅ  ꜱᴛʀᴇᴀᴍᴀʙʟᴇ  ʟɪɴᴋ.',
        reply_markup=button
    )


@StreamBot.on_message((filters.command("help")) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://graph.org/file/a8095ab3c9202607e78ad.jpg",
                caption=f"{m.from_user.mention},\n\n<b><i>⚠️ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ.</i></b>\n\n<i>ᴅᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 😊</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔   ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ   ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ [ᴏᴡɴᴇʀ](https://telegram.me/Mr_SPIDY).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>Share any file with me, and I'll give you a direct download link and a streaming link.</b>

<i>This link can be used to download the file or to stream it directly using an external video player on my servers.
For streaming: Simply copy and paste the link into your video player to start streaming.</i>""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻 Owner", url="https://telegram.me/Mr_SPIDY")],
                [InlineKeyboardButton("💥 Update", url="https://telegram.me/YourDemandZone")]
            ]
        )
    )

@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)