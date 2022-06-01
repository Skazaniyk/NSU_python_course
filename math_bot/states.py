from aiogram.dispatcher.filters.state import State, StatesGroup


class SymplifyState(StatesGroup):
    expression_to_simplify = State()


class DerivativeState(StatesGroup):
    expression_to_differentiation = State()


class IntegralState(StatesGroup):
    expression_to_integration = State()


class EquationsState(StatesGroup):
    expression_to_solve_equations = State()
