import asyncio
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.utils import executor

from config import TOKEN
from keybords import *
from states import SymplifyState, EquationsState, IntegralState, DerivativeState

from sympy import *

x = symbols('x')

loop = asyncio.get_event_loop()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(Command('start'))
async def process_start_command(message: types.Message):
    text = '''Привет! Чем я могу помочь тебе?
Я могу работать только с выражениями, зависящами от Х
        '''

    await message.reply(text, reply_markup=get_bot_menu)


@dp.message_handler(Command('help'))
async def process_help_command(message: types.Message):
    text = '''
Я могу:
1) Упрощать выражения
2) Вычислять производные
3) Вычислять интегралы не определённый
4) Решать уравнения
    '''

    await message.reply(text, reply_markup=get_bot_menu)


@dp.message_handler(Text(equals=['Начать']))
async def process_start_command(message: types.Message):
    text = '''Привет! Чем я могу помочь тебе?
Я могу работать только с выражениями, зависящами от Х

Чтобы начать выбери один из следующих пунктов на клавиатуре:
1) Упрощать выражения
2) Вычислять производные
3) Вычислять интегралы не определённый
4) Решать уравнения
    '''

    await message.reply(text, reply_markup=get_bot_menu)


@dp.message_handler(Text(equals=['Упростить выражение']))
async def cmd_dialog_simplify(message: types.Message):
    await SymplifyState.expression_to_simplify.set()
    await message.reply('Введи выражение, чтобы я его упростил', reply=False)


@dp.message_handler(state=SymplifyState.expression_to_simplify)
async def simplify_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        expression = parse_expr(message.text, transformations='all')
        expression.simplify()
        await message.reply(expression, reply=False)
        await state.reset_state()


@dp.message_handler(Text(equals=['Вычислить производную']))
async def cmd_dialog_derivative(message: types.Message):
    await DerivativeState.expression_to_differentiation.set()
    await message.reply('Введи выражение, чтобы я его продифференцировал', reply=False)


@dp.message_handler(state=DerivativeState.expression_to_differentiation)
async def differentiation_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        expression = parse_expr(message.text, transformations='all')
        differential = diff(expression, x)
        await message.reply(differential, reply=False)
        await state.reset_state()


@dp.message_handler(Text(equals=['Вычислить неопределённый интеграл']))
async def cmd_dialog_integration(message: types.Message):
    await IntegralState.expression_to_integration.set()
    await message.reply('Введи выражение, чтобы я его проинтегрировал', reply=False)


@dp.message_handler(state=IntegralState.expression_to_integration)
async def integration_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        expression = parse_expr(message.text, transformations='all')
        integral = integrate(expression, x)
        await message.reply(integral, reply=False)
        await state.reset_state()


@dp.message_handler(Text(equals=['Решить уравнение']))
async def cmd_dialog_equations(message: types.Message):
    await EquationsState.expression_to_solve_equations.set()
    await message.reply('Введи уравнение, зависящие от Х, чтобы я его решил', reply=False)


@dp.message_handler(state=EquationsState.expression_to_solve_equations)
async def equations_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        expression = parse_expr(message.text, transformations='all')
        solved = solve(expression, x)
        await message.reply(solved, reply=False)
        await state.reset_state()


if __name__ == '__main__':
    executor.start_polling(dp)
