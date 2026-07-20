from aiogram.fsm.state import State, StatesGroup


class ApplicationState(StatesGroup):
    waiting_application = State()