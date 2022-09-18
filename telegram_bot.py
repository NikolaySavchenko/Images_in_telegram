import telegram
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    load_dotenv()
    space_bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    # updates = space_bot.get_updates()
    # space_bot.send_message(text="Hi Peopple! I'm new admin!", chat_id='@space_view')
