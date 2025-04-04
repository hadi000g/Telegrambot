from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup

# تابعی که خبرها رو از سایت می‌گیره
def get_news():
    url = "https://www.yjc.ir/fa"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("a", class_="title")
    news = [title.text.strip() for title in titles[:5]]
    return news

# پاسخ به /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من ربات خبری هستم. دستور /news رو بفرست تا خبرهای جدید رو بفرستم.")

# پاسخ به /news
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news_list = get_news()
    message = "\n\n".join([f"{i+1}. {t}" for i, t in enumerate(news_list)])
    await update.message.reply_text("تیتر خبرهای جدید:\n\n" + message)

# 🔴 🔴 🔴 اینجا توکن خودت رو جایگزین کن
TOKEN = "7980248087:AAHCoYStjJl1I3ZsJcBkBAP8Ua8Sn7lbMNw"

# ساخت و اجرای بات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))

print("✅ ربات روشن شد. منتظر پیام‌ها هستم...")
app.run_polling()