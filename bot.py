import telebot
import os
from flask import Flask, request

# 🔑 Render Environment Variable থেকে Bot Token নিচ্ছে
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# 🧩 Flask অ্যাপ তৈরি
app = Flask(__name__)

@app.route('/')
def home():
    return "🎬 New Movie Bot is Live and Running!"

# 📩 Telegram webhook route
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# ▶️ /start কমান্ড
@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🎬 **স্বাগতম!** 🎬\n\n"
        "🌟 *New Movie Bot*-এ আপনাকে স্বাগতম!\n\n"
        "🍿 এখানে পাবেন নতুন মুভি, বাংলা ডাব, ওয়েব সিরিজ ও সিনেমার লিংক। নিচের অপশন থেকে বেছে নিন 👇"
    )

    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        telebot.types.InlineKeyboardButton("🎥 Hindi Movie Link", url="https://t.me/viralhindimovielink"),
        telebot.types.InlineKeyboardButton("🎬 Tamil & Bangla Movie", url="https://t.me/viraltamilmovielink"),
        telebot.types.InlineKeyboardButton("🎞 English Movie Link", url="https://t.me/viralenglishmovielink"),
        telebot.types.InlineKeyboardButton("📺 Bangla Movie Link", url="https://t.me/viralbanglamovielink"),
        telebot.types.InlineKeyboardButton("🔥 Hot Movie Link", url="https://t.me/viralhotmovielink"),
        telebot.types.InlineKeyboardButton("📺 Web Series & Natok", url="https://t.me/viralnatoklinkweb")
    )

    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode="Markdown",
        reply_markup=markup
    )

# 🚀 Render সার্ভারে চালু করার জন্য কোড
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    bot.remove_webhook()
    bot.set_webhook(url=f'https://new-movie-bot-ddqu.onrender.com/{BOT_TOKEN}')
    app.run(host="0.0.0.0", port=port)
