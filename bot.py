import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")

print("TOKEN:", TOKEN is not None, flush=True)

bot = telebot.TeleBot(TOKEN)

print("PROBANDO TELEGRAM...", flush=True)

try:
    me = bot.get_me()
    print("BOT:", me.username, flush=True)
except Exception as e:
    print("ERROR:", e, flush=True)

import time

while True:
    time.sleep(60)