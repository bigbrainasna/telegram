import os
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler

BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable missing!")
if not ADMIN_USERNAME:
    raise ValueError("❌ ADMIN_USERNAME environment variable missing!")

async def handle_join(update, context):
    user = update.chat_join_request.from_user
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=f"""سلام {user.first_name} عزیز، وقتتون بخیر 🌸

خیلی خوشحالیم که به گروه ما اضافه شدین! 🎉

برای نهایی شدن عضویت، لطفاً یکی از مدارک زیر رو برای @{ADMIN_USERNAME} ارسال کنین:

• رجیستریشن آپرا
• کارت نظام پزشکی  
• کارت دانشجویی معتبر

ممنون از همراهیتون 🙏

در صورت هرگونه سوال می‌تونید با @{ADMIN_USERNAME} در ارتباط باشید."""
        )
    except Exception as e:
        print(f"⚠️ خطا در ارسال پیام به کاربر: {e}")

if __name__ == '__main__':
    print("✅ ربات در حال راه‌اندازی...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join))
    app.run_polling()