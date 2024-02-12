import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler

from bot.bot import start, echo, caps, send_matches, next_game, all_latest_games
from games.api import get_all_matches
from utils import create_txt_file, delete_all_files

load_dotenv()

TELEGRAM_KEY = os.getenv('TELEGRAM_BOT_KEY')


def main():
    delete_all_files()
    create_txt_file('matches', str(get_all_matches()))

    application = ApplicationBuilder().token(TELEGRAM_KEY).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler("caps", caps)
    matches_handler = CommandHandler("matches", send_matches)
    next_game_handler = CommandHandler("next_match", next_game)
    all_latest_game_handler = CommandHandler("latest_matches", all_latest_games)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(matches_handler)
    application.add_handler(next_game_handler)
    application.add_handler(all_latest_game_handler)

    application.run_polling()


main()
