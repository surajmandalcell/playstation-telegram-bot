#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
import os
from dotenv import load_dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

load_dotenv()

telegram_key = os.environ.get("TELEGRAM_KEY")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_key).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()
