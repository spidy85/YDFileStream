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

multi_clients = ["5589458915:AAEqouH2vlQMr4HBplD_0djItSLqqbXC2Oo", "5644449410:AAGFMv5EYtwnDESMTJ0qDKF0Zt-k8SqJj90", "6740108531:AAFgCp_NVCP2jRk4iuWNE9mivFBjCJa1_LY"]
work_loads = {}
