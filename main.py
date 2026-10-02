import os
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
message = update.message
if not message or not message.text:
return

text = message.text

# بحث عن الرمز (أرقام تتراوح بين 4 إلى 6 مراتب كأكواد تحقق)
# ندور على كلمات مفتاحية أو نلتقط الأرقام الصريحة
match = re.search(r'\b\d{4,6}\b', text)

if match:
otp_code = match.group(0)

# إنشاء زر تفاعلي للنسخ السريع (أو إظهار الكود بشكل بارز)
keyboard = [[InlineKeyboardButton(f"📋 نسخ الرمز: {otp_code}", callback_data=otp_code)]]
reply_markup = InlineKeyboardMarkup(keyboard)

# إرسال الكود الصافي للمجموعة مع الزر
await message.reply_text(
f"🔐 رمز التحقق المستخرج:\n{otp_code}",
parse_mode="Markdown",
reply_markup=reply_markup
)

def main():
app = ApplicationBuilder().token(TOKEN).build()

# مراقبة كل الرسائل اللي توصل للجروب (حتى من التطبيقات والبوتات الأخرى)
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("Bot is running...")
app.run_polling()

if name == "main":
main()