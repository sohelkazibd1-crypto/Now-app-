from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome! Open Mini App to manage balance & levels.")

app = ApplicationBuilder().token("8433024749:AAE8sjKTbwjq6oyaPkhnrvG0ZagCfuhWDNA").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()