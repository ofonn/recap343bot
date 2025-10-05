from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")


# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Main formatted text (like the screenshot)
    message_text = (
        "➡️ Code : https://link-center.net/1227837/how-to-unlock-full-access5\n\n"
        "➡️ Mega : https://mega.nz/folder/xNBjxAQR\n\n"
        "Share the group 3 times to unlock all the special content 🤫"
    )

    # Inline buttons (second section)
    unlock_keyboard = [
        [InlineKeyboardButton("Group To Unlock 🔒", url="https://t.me/share/url?url=https://t.me/recap343bot")],
        [InlineKeyboardButton("Free Extracts 😋", url="https://t.me/recap343bot")],
        [InlineKeyboardButton("10 Free Gifs 🎁", url="https://t.me/recap343bot")]
    ]
    unlock_markup = InlineKeyboardMarkup(unlock_keyboard)

    # Send main message (links + instruction)
    await update.message.reply_text(
        message_text,
        disable_web_page_preview=True
    )

    # Send the 3 inline buttons below
    await update.message.reply_text(
        " ",
        reply_markup=unlock_markup,
        disable_web_page_preview=True
    )

    # Send plain “Main Menu” text
    await update.message.reply_text(
        "🔝 Main Menu",
        disable_web_page_preview=True
    )


# --- Fallback for any text message ---
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
