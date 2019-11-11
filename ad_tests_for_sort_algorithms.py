from random import randint
import sys
from 02_insertion_sort import insertion_sort


def random_list(items_count=5):
    """
    возврящает список размером items_count состоящий из случайных целых чисел
    в диапазоне от (-100 : 100)
    """
    return [randint(-100, 100) for x in range(items_count)]


def colored_print(what_print):
    """
    печатает ОК зеленым а Fail красным
    :param what_print: что печатаем
    :param color: каким цветом
    """
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"
    if what_print == 'Fail':
        sys.stdout.write(RED)
        print('Fail')
    elif what_print == 'OK':
        sys.stdout.write(GREEN)
        print('OK')
    else:
        sys.stdout.write(RESET)
        print(what_print)
    sys.stdout.write(RESET)
    return ''


def test_sort(sort_algorithm):
    """ тестирует функции сортировки """
    sys.stdout.write("\033[1;34m")
    print("Тестирую:", sort_algorithm.__doc__, sep='')
    sys.stdout.write("\033[0;0m")
    for test_number in range(1, 4):
        print("testcase #", test_number, ":", sep='')
        input_list = random_list()
        print("start list ", input_list)
        sorted_list = sort_algorithm(input_list)
        print("sorted list", sorted_list)
        check_list = sorted(input_list)
        print("check list ", check_list)
        print('Status: ', end='')
        print(colored_print('OK') if sorted_list == check_list else colored_print('Fail'))

test_sort(insertion_sort)
test_sort(choice_sort)
test_sort(bubble_sort)
