from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")

# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    inline_keyboard = [
        [InlineKeyboardButton("➡️ Code", url="https://link-center.net/123456/how-to-unlock-full-access5")],
        [InlineKeyboardButton("➡️ Mega", url="https://mega.nz/folder/xxxxx")],
        [InlineKeyboardButton("➡️ Share 3 Times", url="https://t.me/share/url?url=https://t.me/recap343bot")]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    reply_keyboard = [[KeyboardButton("Main Menu")]]
    menu_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome 🎉\n\nClick a button below to continue:",
        reply_markup=inline_markup
    )
    await update.message.reply_text(
        "Choose an option:",
        reply_markup=menu_markup
    )

# --- Fallback for any message ---
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