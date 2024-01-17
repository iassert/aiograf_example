from aiogram.types      import Message as aiogramMessage
from aiogram.dispatcher import FSMContext

from ..Accest.translation import ttr

from aiograf.bot   import ManageBot
from aiograf.types import Message

from config import Config


class Main:
	mbot: ManageBot = ManageBot()
	mbot.init(Config.TOKEN, server = Config.LOCAL_SERVER)

	async def start(message: aiogramMessage, state: FSMContext):
		message: Message = Message(message)
		await message.answer(ttr.start)

	def main():
		Main.mbot.start_polling(
			on_startup_  = Main.mbot.on_startup(Config.CREATOR_ID),
			on_shutdown_ = Main.mbot.on_shutdown(Config.CREATOR_ID)
		)
