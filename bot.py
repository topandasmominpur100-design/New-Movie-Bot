import os
import telebot
from telebot import types

# Get token from environment variable (Render) or replace the placeholder locally
TOKEN = os.getenv("BOT_TOKEN", "8409926523:AAFpAAyF2TAdunT4AHHTpwAqPingCCk_x74")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = (
        "🎉 স্বাগতম!\n\n"
        "🍿 New Movie Bot-এ আপনাকে স্বাগতম!\n\n"
        "আপনার পছন্দের মুভি, ওয়েব সিরিজ এবং নাটকের লিঙ্ক পেতে নিচের রঙিন বোতামগুলো থেকে বেছে নিন 👇"
    )

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🟥  Hindi Movie Link 🎥", url="https://t.me/viralhindimovielink"),
        types.InlineKeyboardButton("🟧  Tamil & Bangla Movie 🎞", url="https://t.me/viraltamilmovielink"),
        types.InlineKeyboardButton("🟨  English Movie Link 🍿", url="https://t.me/viralenglishmovielink"),
        types.InlineKeyboardButton("🟩  Bangla Movie Link 🎭", url="https://t.me/viralbanglamovielink"),
        types.InlineKeyboardButton("🟦  Hot Movie Link 🔥", url="https://t.me/viralhotmovielink"),
        types.InlineKeyboardButton("🟪  Web Series & Natok 📺", url="https://t.me/viralnatoklinkweb")
    )

    # send message without parse_mode to avoid entity parsing errors
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

if __name__ == '__main__':
    print("🚀 New Movie Bot is starting...")
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("Bot stopped with error:", e)
