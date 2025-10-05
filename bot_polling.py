from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# --- Your Bot Token ---
TOKEN = "8233593403:AAEuSHDANqfJoek7HuJ11pu4kDeKawyzCd8"

# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Inline buttons (like in your screenshot)
    keyboard = [
        [InlineKeyboardButton("➡️ Code", url="https://link-center.net/123456/how-to-unlock-full-access5")],
        [InlineKeyboardButton("➡️ Mega", url="https://mega.nz/folder/xxxxx")],
        [InlineKeyboardButton("➡️ Share 3 Times", url="https://t.me/share/url?url=https://t.me/recap343bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Reply button (Main Menu at bottom)
    reply_keyboard = [[KeyboardButton("Main Menu")]]
    reply_markup_keyboard = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

    # Send welcome message with inline buttons
    await update.message.reply_text(
        "Welcome 🎉\n\nClick a button below to continue:",
        reply_markup=reply_markup
    )

    # Send "Main Menu" button separately
    await update.message.reply_text(
        "Choose an option:",
        reply_markup=reply_markup_keyboard
    )

# --- Fallback for any message (always show menu) ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

# --- Main function ---
def main():
    app = Application.builder().token(TOKEN).build()

    # /start command
    app.add_handler(CommandHandler("start", start))

    # Any text triggers welcome again
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
