from telegram import (
    Update,
    ReplyKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from scraper import get_all_prices
from formatter import market_message
from compare import compare_prices
from gist_cache import load_cache
from config import BOT_TOKEN


keyboard = ReplyKeyboardMarkup(
    [
        ["📊 قیمت لحظه‌ای"],
        ["💵 دلار", "💶 یورو"],
        ["🥇 طلا", "🪙 سکه"]
    ],
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "به ربات بازار خوش آمدید.",
        reply_markup=keyboard
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    prices = get_all_prices()

    cache = load_cache()

    last = cache.get("last", {})

    _, changes = compare_prices(
        prices,
        last
    )

    msg = market_message(
        prices,
        changes
    )

    await update.message.reply_text(msg)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    prices = get_all_prices()

    if text == "📊 قیمت لحظه‌ای":

        cache = load_cache()

        last = cache.get("last", {})

        _, changes = compare_prices(
            prices,
            last
        )

        await update.message.reply_text(
            market_message(
                prices,
                changes
            )
        )

    elif text == "💵 دلار":

        await update.message.reply_text(prices["usd"])

    elif text == "💶 یورو":

        await update.message.reply_text(prices["eur"])

    elif text == "🥇 طلا":

        await update.message.reply_text(prices["gold18"])

    elif text == "🪙 سکه":

        await update.message.reply_text(prices["coin"])


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(
    MessageHandler(
        filters.TEXT,
        menu
    )
)

app.run_polling()
