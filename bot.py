# bot.py

import asyncio
from telegram import (
    Bot,
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from scraper import get_all_prices
from coinmarketcap_scraper import get_crypto_prices
from formatter import market_message
from sender import send
from gist_cache import load_cache, save_cache
from compare import compare_prices
from config import CHANNELS, BOT_TOKEN


# ------------------------------
# ساخت پیام قیمت
# ------------------------------

def build_market_message():

    prices = get_all_prices()
    crypto = get_crypto_prices()

    prices.update(crypto)

    cache = load_cache()
    last_prices = cache.get("last", {}) if cache else {}

    used_cache = False

    for key in prices:

        if prices[key] == "ERROR" and key in last_prices:

            prices[key] = last_prices[key]
            used_cache = True

    changed, changes = compare_prices(prices, last_prices)

    if "ERROR" not in prices.values():
        save_cache(prices)

    message = market_message(prices, changes)

    return message


# ------------------------------
# ارسال به کانال
# ------------------------------

async def channel_sender():

    message = build_market_message()

    await send(CHANNELS, message)


# ------------------------------
# دکمه شیشه‌ای
# ------------------------------

def keyboard():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "💰 دریافت قیمت لحظه‌ای",
                    callback_data="price"
                )
            ]
        ]
    )


# ------------------------------
# /start
# ------------------------------

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "سلام 👋",
        reply_markup=keyboard()
    )


# ------------------------------
# /price
# ------------------------------

async def price(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text("⏳ در حال دریافت قیمت...")

    message = build_market_message()

    await update.message.reply_text(
        message,
        reply_markup=keyboard()
    )


# ------------------------------
# دکمه
# ------------------------------

async def callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    if query.data == "price":

        await query.edit_message_text(
            "⏳ در حال دریافت قیمت..."
        )

        message = build_market_message()

        await query.message.reply_text(
            message,
            reply_markup=keyboard()
        )


# ------------------------------
# اجرا
# ------------------------------

async def main():

    await channel_sender()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CallbackQueryHandler(callback))

    print("BOT STARTED")

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
