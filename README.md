# New Movie Bot (Render-ready)

This repository contains a simple Telegram bot (New Movie Bot) ready to deploy on Render or any other Python host.

## Files
- `bot.py` - the main bot script
- `requirements.txt` - required Python package
- `.gitignore` - ignore patterns

## Setup (Local / PyDroid)
1. Install dependency:
```
pip install -r requirements.txt
```
2. Open `bot.py` and replace the token placeholder:
```py
TOKEN = os.getenv("BOT_TOKEN", "REPLACE_WITH_YOUR_TOKEN")
```
You can either:
- Replace `"REPLACE_WITH_YOUR_TOKEN"` with your bot token (only for local testing), **or**
- Set an environment variable `BOT_TOKEN` (recommended).

3. Run:
```
python bot.py
```

## Deploy to Render.com (24/7 uptime)
1. Create a GitHub repo and upload these files.
2. On Render.com, create a **New Web Service** and connect your GitHub repo.
3. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`
4. Add an Environment Variable in Render:
   - Key: `BOT_TOKEN`
   - Value: `<your-telegram-bot-token>`
5. Deploy. Render will run the bot 24/7.

## Security
- **Do NOT** publish your bot token in public places. Use environment variables (Render) or `.env` locally.
- If your token was exposed, regenerate it via `@BotFather`.

If you want, replace the button labels or channel links in `bot.py`.