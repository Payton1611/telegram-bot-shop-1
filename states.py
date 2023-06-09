
from aiogram.dispatcher.filters.state import StatesGroup, State

class Puchase(StatesGroup):
    EnterQuantity: State()
    Approval = State()
    Payment = State()

class NewItem(StatesGroup):
    Name = State()
    Photo = State()
    Price = State()
    Confirm = State()

class DeleteItem(StatesGroup):
    Delete_Item = State()

