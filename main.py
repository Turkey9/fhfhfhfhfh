import config
import time
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()
app = Client(
    "Anonymous",
    api_id=config.18189325,
    api_hash=config.7cb3b3ea70ba49f0721a511013eefe53,
    bot_token=config.6048858444:AAFNQyUMKCdMEsJvaGXoaZAJ7ObrGpr51_E,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("Starting the String Generator Bot...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("Bot stopped. Bye !")
