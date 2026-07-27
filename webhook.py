import os
import asyncio

from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from scraper import get_prices
from formatter import build_message

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

PORT = int(os.getenv("PORT", 10000))

app = FastAPI()

telegram_app = Application.builder().token(BOT_TOKEN).build()


# --------------------------
# COMMANDS
# --------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "سلام 👋\n\n"
        "دستورات:\n\n"
        "/price  قیمت لحظه‌ای"
    )

    await update.message.reply_text(text)


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        prices = get_prices()

        message = build_message(prices)

        await update.message.reply_text(message)

    except Exception as e:

        await update.message.reply_text(
            f"❌ خطا در دریافت قیمت‌ها\n\n{e}"
        )


telegram_app.add_handler(CommandHandler("start", start))
telegram_app.add_handler(CommandHandler("price", price))


# --------------------------
# FASTAPI
# --------------------------

@app.on_event("startup")
async def startup():

    await telegram_app.initialize()

    await telegram_app.start()

    await telegram_app.bot.set_webhook(
        url=f"{WEBHOOK_URL}/webhook"
    )

    print("Webhook Set")


@app.on_event("shutdown")
async def shutdown():

    await telegram_app.stop()

    await telegram_app.shutdown()


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    update = Update.de_json(
        data,
        telegram_app.bot,
    )

    await telegram_app.process_update(update)

    return {
        "ok": True
    }


@app.get("/")
async def root():

    return {
        "status": "running"
    }


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "webhook:app",
        host="0.0.0.0",
        port=PORT,
    )
