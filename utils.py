from transitions import Machine


class Pizza(object):
    pass


size = Pizza()


class Payment(object):
    pass


payment = Payment()

states = ['empty', 'большую', 'маленькую', 'картой', 'наличкой']

# Таблица переходов.
transitions = [
    # Состояния размеров пиццы.
    {'trigger': "small_size", "source": 'empty', 'dest': 'маленькую'},
    {'trigger': "big_size", "source": 'empty', 'dest': 'большую'},
    # Состояния способов оплаты.
    {'trigger': "cash", "source": 'empty', 'dest': 'наличкой'},
    {'trigger': "card", "source": 'empty', 'dest': 'картой'}
]


# Инициализируем стейт машину.
def initial_the_machine():
    machine = Machine(Pizza, states=states, transitions=transitions, initial='empty')

    payment_machine = Machine(Payment, states=states, transitions=transitions, initial='empty')
