from ..Handlers.main import Main

Main.mbot.dp.register_message_handler(
    Main.start,
    commands = "start",
    state = "*"
)
