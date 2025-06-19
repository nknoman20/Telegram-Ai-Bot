import os
import logging
import asyncio
from dotenv import load_dotenv
from ai_engine import get_ai_response
from translator import translate_text
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DEFAULT_LANG = os.getenv("DEFAULT_LANG", "en")

# Logging config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    user_lang = update.message.from_user.language_code or DEFAULT_LANG

    try:
        translated_input = translate_text(user_msg, target_lang="en")
        ai_response = get_ai_response(translated_input)
        translated_output = translate_text(ai_response, target_lang=user_lang)
        await update.message.reply_text(translated_output)
    except Exception as e:
        await update.message.reply_text("⚠️ দুঃখিত, কিছু ভুল হয়েছে। পরে আবার চেষ্টা করুন।")
        logging.error(e)

# Async bot runner
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

# Entry point
if __name__ == '__main__':
    keep_alive()
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except RuntimeError as e:
        print(f"Event loop error: {e}")
