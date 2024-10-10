#(c) @Mr_SPIDY
import os
import asyncio
from asyncio import TimeoutError
from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


MY_PASS = os.environ.get("MY_PASS", 'SpikA')
pass_db = Database(Var.DATABASE_URL, "ag_passwords")

@StreamBot.on_message(filters.command("login") & filters.private, group=4)
async def login_handler(c: Client, m: Message):
    ag = await m.reply_text(
        "Please send me the password.\n\nIf you don't know it, check the MY_PASS variable in Heroku.\n"
        "(You can use /cancel to cancel the process.)"
    )
    try:
        _text = await c.listen(m.chat.id, filters.text, timeout=90)
        if _text.text == "/cancel":
            await ag.edit("Process Cancelled Successfully.")
            return

        textp = _text.text
        if textp == MY_PASS:
            await pass_db.add_user_pass(m.chat.id, textp)
            await ag.edit("Yeah! You entered the password correctly.")
        else:
            await ag.edit("Wrong password, please try again.")
    except asyncio.TimeoutError:
        await ag.edit("I can't wait any longer for the password. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
        await ag.edit("An error occurred, please try again later.")

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.photo), group=4)
async def private_receive_handler(c: Client, m: Message):
    check_pass = await pass_db.get_user_pass(m.chat.id)
    
    if not check_pass:
        await m.reply_text("Please log in first using the /login command.\nIf you don't know the password, request it from the developer.")
        return
    elif check_pass != MY_PASS:
        await pass_db.delete_user(m.chat.id)
        await m.reply_text("Session expired. Please log in again.")
        return
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Contact Developer [⚝𝗠𝗿.𝗦𝗣𝗜𝗗𝗬⚝](https://telegram.me/Mr_SPIDY) he will help you.**",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<b>ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔  ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ  ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="**sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍʏ [ʙᴏss](https://telegram.me/Mr_SPIDY)**",
                
                disable_web_page_preview=True)
            return
    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}/watch/{str(log_msg.id)}/YDMovieZone.mkv?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}/{get_hash(log_msg)}{str(log_msg.id)}"
        
        msg_text ="""
<b>ʏᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡</b>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i>{}</i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b>⚠️ ᴛʜɪꜱ ʟɪɴᴋ ᴡɪʟʟ ᴇxᴘɪʀᴇ ᴀꜰᴛᴇʀ 𝟷𝟸 ʜᴏᴜʀꜱ</b>

<b>❇️  ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : @YourDemandZone</b>"""

        a=await log_msg.reply_text(text=f"**ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True,  quote=True)
        k=await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), stream_link, online_link),
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ꜱᴛʀᴇᴀᴍ  🖥️", url=stream_link),
                 InlineKeyboardButton('📥  ᴅᴏᴡɴʟᴏᴀᴅ  📥', url=online_link)],
                [InlineKeyboardButton('Share URL', url=f"https://t.me/share/url?url={online_link}")]])
        )
        await asyncio.sleep(43200)
        await log_msg.delete()
        await a.delete()
        await m.delete()
        await k.delete()
    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(chat_id=Var.BIN_CHANNEL, text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n**𝚄𝚜𝚎𝚛 𝙸𝙳 :** `{str(m.from_user.id)}`", disable_web_page_preview=True)


@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if MY_PASS:
        check_pass = await pass_db.get_user_pass(broadcast.chat.id)
        if check_pass == None:
            await broadcast.reply_text("Login first using /login cmd \n don\'t know the pass? request it from developer!")
            return
        if check_pass != MY_PASS:
            await broadcast.reply_text("Wrong password, login again")
            await pass_db.delete_user(broadcast.chat.id)
            
            return
    if int(broadcast.chat.id) in Var.BANNED_CHANNELS:
        await bot.leave_chat(broadcast.chat.id)
        
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**ʀᴇǫᴜᴇꜱᴛ ᴜʀʟ:** {stream_link}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ꜱᴛʀᴇᴀᴍ  🖥️", url=stream_link),
                     InlineKeyboardButton('📥  ᴅᴏᴡɴʟᴏᴀᴅ  📥', url=online_link)]
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ERROR_TRACKEBACK:** `{e}`", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{e}**")