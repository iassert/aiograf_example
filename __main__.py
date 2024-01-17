from src.Handlers.main       import Main
from src.Registers.registers import *

from aiograf.bot.api import log
from aiograf.bot.noraiseclass import noraiseclass

log.init(__file__)
noraiseclass.init(is_rise = False)

if __name__ == "__main__":
    Main.main()
