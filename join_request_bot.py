import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(f"Hello {user.first_name}! Your join request has been received.")

async def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(MessageHandler(Filters.all, handle_join_request))
    
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())  # This is the correct way to run async code