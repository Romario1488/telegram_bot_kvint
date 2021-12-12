from utils import *


def test(pizza_size, pay):
    initial_the_machine()  # Инициализируем стейт машину

    # Проверка условий
    if pizza_size == 'большую':
        size.big_size()
    elif pizza_size == 'маленькую':
        size.small_size()
    else:
        print('Invalid value for pizza_size')

    if pay == "картой":
        payment.card()
    elif pay == 'наличкой':
        payment.cash()
    else:
        print('Invalid value for payment')

    # Результат теста
    print(f'Size: {size.state}, Payment: {payment.state}')


# При вызове функции передаем два параметра
# размер пиццы: маленькую/большую
# способ оплаты: наличкой/картой
test('большую', 'картой')
test('большую', 'наличкой')
test('маленькую', 'наличкой')
test('маленькую', 'картой')
