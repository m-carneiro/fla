import logging

from telegram import Update
from telegram.ext import ContextTypes

from bot.content import beautify_matches, next_match, recent_matches

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def send_matches(update: Update, context: ContextTypes.DEFAULT_TYPE):
    matches = beautify_matches()
    for match in matches:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=match)


async def next_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    match = next_match()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=match)


async def all_latest_games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    latest_matches = recent_matches()
    for match in latest_matches:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=match)
