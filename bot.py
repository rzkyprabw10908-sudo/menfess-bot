from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN ="8842155091:AAGk0x-v0J4GVpmGG5D3ut_fWgzDuvdCtKM"
CHANNEL_ID = "@menfesshamabeeska"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("kirim pesan menfess kamu")

async def kirim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=pesan
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, kirim))

print("bot nyala...")
app.run_polling()
