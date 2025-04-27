import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = os.environ['BOT_TOKEN']
ADMIN_USERNAME = os.environ['ADMIN_USERNAME']

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=f"Hi {user.first_name}! Please message @{ADMIN_USERNAME} to complete verification to join the group."
        )
    except Exception as e:
        print(f"Failed to message {user.username}: {e}")

def run_bot():
    """Run the bot synchronously for Railway compatibility"""
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(ChatJoinRequestHandler(handle_join_request))
    
    # This will handle the event loop internally
    application.run_polling()

if __name__ == '__main__':
    run_bot()  # Simplified entry point