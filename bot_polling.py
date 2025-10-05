# bot_polling.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")


# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Main formatted text
    message_text = (
        "➡️ Code : https://link-center.net/1227837/how-to-unlock-full-access5\n\n"
        "➡️ Mega : https://mega.nz/folder/xNDPjxAQR\n\n"
        "Share the group 3 times to unlock all the special content 🤫"
    )

    # Inline buttons (under the text)
    keyboard = [
        [InlineKeyboardButton("Group To Unlock 🔒", url="https://t.me/recap343bot")],
        [InlineKeyboardButton("Free Extracts 😊", url="https://mega.nz/folder/xNDPjxAQR")],
        [InlineKeyboardButton("10 Free Gifs 🎁", url="https://link-center.net/1227837/how-to-unlock-full-access5")],
    ]
    inline_markup = InlineKeyboardMarkup(keyboard)

    # Send main message with inline buttons
    await update.message.reply_text(
        message_text,
        reply_markup=inline_markup,
        disable_web_page_preview=True
    )

    # Send plain “Main Menu” text below
    await update.message.reply_text(
        "🔝 Main Menu",
        disable_web_page_preview=True
    )


# --- Handle any normal text by showing the menu again ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# --- Main function ---
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
