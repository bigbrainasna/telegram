import os
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

async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(ChatJoinRequestHandler(handle_join_request))

    # Use run_polling() without asyncio.run
    await application.run_polling()

    # Optionally, you can add idle to keep the bot running
    await application.idle()

# Directly call the main function without asyncio.run()
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()  # Get the current event loop
    loop.run_until_complete(main())  # Run the main function in the existing loop

