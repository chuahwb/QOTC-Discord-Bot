from bot.bot import setup_bot
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    bot = setup_bot()
    bot.run(token=TOKEN)


if __name__ == '__main__':
    main()
