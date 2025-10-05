# bot_polling_fixed.py
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise ValueError("BOT_TOKEN not found! Please set it as an environment variable.")


def _get_chat(update: Update):
    """Return a Chat object safely from various update types (message, callback_query...)."""
    if update.effective_chat:
        return update.effective_chat
    if getattr(update, "message", None) and update.message.chat:
        return update.message.chat
    if getattr(update, "callback_query", None) and update.callback_query.message and update.callback_query.message.chat:
        return update.callback_query.message.chat
    return None


# --- Welcome Message Function ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = _get_chat(update)
    if chat is None:
        logger.warning("No chat available for this update; skipping start()")
        return

    # --- Main formatted text (like the screenshot) ---
    message_text = (
        "➡️ Code : https://link-center.net/1227837/how-to-unlock-full-access5\n\n"
        "➡️ Mega : https://mega.nz/folder/xNBjxAQR\n\n"
        "Share the group 3 times to unlock all the special content 🤫"
    )

    # --- Inline buttons section (three buttons) ---
    unlock_keyboard = [
        [InlineKeyboardButton("Group To Unlock 🔒", url="https://t.me/share/url?url=https://t.me/recap343bot")],
        [InlineKeyboardButton("Free Extracts 😋", url="https://t.me/recap343bot")],
        [InlineKeyboardButton("10 Free Gifs 🎁", url="https://t.me/recap343bot")]
    ]
    unlock_markup = InlineKeyboardMarkup(unlock_keyboard)

    try:
        # 1) Send the main text block (no preview)
        sent_main = await chat.send_message(
            text=message_text,
            disable_web_page_preview=True
        )
        logger.info("Sent main text message (id=%s)", getattr(sent_main, "message_id", None))

        # 2) Send the inline buttons attached to a non-empty message.
        # Use a zero-width space so Telegram will display the message and attach the keyboard.
        zero_width = "\u200b"
        sent_buttons = await chat.send_message(
            text=zero_width,
            reply_markup=unlock_markup,
            disable_web_page_preview=True
        )
        logger.info("Sent buttons message (id=%s)", getattr(sent_buttons, "message_id", None))

        # 3) Send the plain "Main Menu" text
        sent_menu = await chat.send_message(
            text="🔝 Main Menu",
            disable_web_page_preview=True
        )
        logger.info("Sent main menu text (id=%s)", getattr(sent_menu, "message_id", None))

    except Exception as e:
        logger.exception("Failed to send the full menu flow: %s", e)
        # Attempt fallbacks so the user still sees something
        try:
            await chat.send_message(text=message_text, disable_web_page_preview=True)
        except Exception:
            logger.exception("Fallback: sending main text failed too.")


# --- Fallback for any text message ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)


# --- Main function ---
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
