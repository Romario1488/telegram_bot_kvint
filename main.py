import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from keyboards import size_keyboard, payment_keyboard, confirm_an_order
from utils import *

API_TOKEN = TOKEN


class Bot(object):
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Инициализируем бота и диспетчер
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    def initialize(self):
        executor.start_polling(self.dp, skip_updates=True)

    # Обработчик сообщений
    @dp.message_handler()
    async def message(self: types.Message):
        if self.text == '/start':
            initial_the_machine()  # Инициализируем стейт машину
            await self.answer('Здравствуйте, какую пиццу вы хотите?',
                              reply_markup=size_keyboard())

        elif self.text == "Маленькую":
            size.small_size()  # Изменяем состояние стейт машины
            await self.answer('Как вы будете платить?', reply_markup=payment_keyboard())

        elif self.text == "Большую":
            size.big_size()  # Изменяем состояние стейт машины
            await self.answer('Как вы будете платить?', reply_markup=payment_keyboard())

        elif self.text == "Наличкой":
            payment.cash()  # Изменяем состояние стейт машины
            await self.answer(f'Вы хотите {size.state} пиццу, оплата - {payment.state}?',
                              reply_markup=confirm_an_order())

        elif self.text == "Картой":
            payment.card()  # Изменяем состояние стейт машины
            await self.answer(f'Вы хотите {size.state} пиццу, оплата - {payment.state}?',
                              reply_markup=confirm_an_order())

        elif self.text == 'Да':
            await self.answer('Спасибо за заказ', reply_markup=types.ReplyKeyboardRemove())

        elif self.text == 'Нет':
            initial_the_machine()  # Заново вызываем инициализацию стейт машины
            await self.answer('Отмена заказа\nКакую пиццу вы хотите?', reply_markup=size_keyboard())
        return


if __name__ == "__main__":
    handler = Bot()
    # Проверяем, чтобы  handler наследовался от базового класса Bot
    if isinstance(handler, Bot):
        # Вызываем функцию, запускающую пуллинг
        handler.initialize()
