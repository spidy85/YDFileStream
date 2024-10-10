# (c) @Mr_SPIDY
from pyrogram import Client
import pyromod.listen
from ..vars import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = ["7243457121:AAGrYohBljhlDZVfsKj8hJXTlby7-nrwojk", "6776232727:AAHV_2j8X_am0lgs6HYKoGFuBK0r0sOBAdw", "6740108531:AAFgCp_NVCP2jRk4iuWNE9mivFBjCJa1_LY","5516461185:AAFR_iOx2RP8N5qehZazh_GkqN2MEGOdQlw", "6147254678:AAHIITj4d0pNGbWeqQtPZD8G6gfUSPE-nWg", "6409608091:AAERZHsXXv4YETHpN5VTEu_-hVoZYwro0O0", "6560035392:AAFLx4WrW5NzZ-oBcJA65qJzn3LtCU5xhhE", "7304146903:AAEgE4L3Y6CxkV1nHVBu5rmzEEb9YZIAAHo" ]
work_loads = {}
