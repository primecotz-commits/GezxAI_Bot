from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to GezxAI_Bot!\n\n"
        "✅ Bot is online."
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("GezxAI_Bot is running...")

app.run_polling()
