import os
import yaml

from aiogram.bot.api import TelegramAPIServer


with open(
    os.path.abspath(__file__).replace(
        os.path.basename(__file__), 
        "config.yaml"
    ), 'r'
) as f:
    load_data: dict[str, str | int] = yaml.load(f, Loader = yaml.FullLoader)


class Config:
    TOKEN:      str = load_data["token"]
    CREATOR_ID: int = load_data["creator_id"]

    LOCAL_SERVER: TelegramAPIServer = TelegramAPIServer.from_base('http://localhost:8081')
