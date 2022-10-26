import controller
import model
import view

test = int(input('Введите версию калькулятора (1 - строчный), (2 - поэтапный): '))
if test == 2:
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total
elif test == 1:
    type(model.calc)
    model.init_calc()
    controller.calc_str()
    view.print_total()
else:
    view.error_version()