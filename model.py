import controller
import view

first = 0
second = 0
ops = ''
total = 0
calc = ''

def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

def init_calc():
    global calc
    calc = str(controller.input_calc('Введите выражение: '))