# bot_polling.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
import os

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")

def get_menu():
    """
    Returns (text, InlineKeyboardMarkup) for the menu so both start()
    and the callback handler can reuse the exact same content.
    """
    text = (
        "➡ Code : https://link-center.net/1227837/how-to-unlock-full-access5\n"
        "➡ Mega : https://mega.nz/folder/xNDPjxAQR\n\n"
        "Share the group 3 times to unlock all the special content 😯"
    )

    # Rows of big buttons (you can change the `url=` values to whatever you want)
    keyboard = [
        [InlineKeyboardButton("Group To Unlock 🔒", url="https://t.me/recap343bot")],
        [InlineKeyboardButton("Free Extracts 😊", url="https://mega.nz/folder/xNDPjxAQR")],
        [InlineKeyboardButton("10 Free Gifs 🎁", url="https://link-center.net/1227837/how-to-unlock-full-access5")],
        # Small "Main Menu" inline button to re-open the menu without creating a new message
        [InlineKeyboardButton("Main Menu", callback_data="MAIN_MENU")],
    ]
    return text, InlineKeyboardMarkup(keyboard)


# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, inline_markup = get_menu()

    # If /start came from a message:
    if update.message:
        await update.message.reply_text(text, reply_markup=inline_markup)
    # If start was invoked from a callback query (just in case), reply on that message
    elif update.callback_query:
        await update.callback_query.message.reply_text(text, reply_markup=inline_markup)


# --- Handle any normal text by showing the menu (same behaviour as before) ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# --- CallbackQuery handler for inline buttons with callback_data ---
async def on_button_pressed(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Stop the loading spinner on the client

    if query.data == "MAIN_MENU":
        # Re-edit the same message to show the menu again (no new bubble)
        text, inline_markup = get_menu()
        try:
            await query.message.edit_text(text, reply_markup=inline_markup)
        except Exception:
            # If edit fails for some reason (message older, etc.), fallback to sending a message
            await query.message.reply_text(text, reply_markup=inline_markup)


# --- Main function ---
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(on_button_pressed))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
