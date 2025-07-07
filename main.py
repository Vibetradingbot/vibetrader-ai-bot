import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")  # Optional: Your Telegram user ID
LICENSE_WALLET = "TYEHLdRv2ZfueZk6YCzsp8ZdpjA6tRP1Bv"  # Your USDT TRC20 wallet

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to VibeTrader AI Bot!\n\n"
        "🚀 Automated Crypto Futures Trading\n"
        "💳 License payment (USDT TRC20):\n"
        f"`{LICENSE_WALLET}`\n\n"
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show help\n"
        "/panel - View admin panel (if admin)\n"
        "/test_trade - Run a demo trade simulation"
    )

async def panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) == ADMIN_ID:
        await update.message.reply_text("📊 Admin Panel:\nUsers: 1\nTrades simulated today: 2\nStatus: Running ✅")
    else:
        await update.message.reply_text("🚫 You are not authorized to access the panel.")

async def test_trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Demo Trade Executed:\n"
        "Pair: BTC/USDT\nType: Long\nEntry: $29,580\nTP: $29,800 ✅\nSL: $29,480\nProfit: +5%"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("panel", panel))
    app.add_handler(CommandHandler("test_trade", test_trade))
    app.run_polling()
