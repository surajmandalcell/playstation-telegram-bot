#!/usr/bin/env python
import os
import requests
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

from utils.fs import object_dump

load_dotenv()

telegram_key = os.environ.get("TELEGRAM_KEY")
platprices_key = os.environ.get("PLATPRICES_KEY")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def game_search(update: Update, context: CallbackContext.DEFAULT_TYPE):
    game = update.message.text.replace("/game ", "")
    data = requests.get(
        f"https://platprices.com/api.php?key={platprices_key}&name={game}"
    )
    object_dump(data.json())
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Details for {game}"
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_key).build()

    application.add_handler(CommandHandler("game", game_search))

    application.run_polling()
