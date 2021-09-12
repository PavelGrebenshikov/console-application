from os import listdir, path, getcwd
from datetime import datetime
from time import time
from sys import platform
import argparse
from glob import glob

def __initialization_arguments():
    """
    Функция инцилизирует аргументы при запуске программы.
    """

    parser = argparse.ArgumentParser()

    # arguments
    parser.add_argument("-b", "--bubbleSort", nargs="+", help="Sorted with help bubble algorithm", type=int)
    parser.add_argument("-t", "--time", help="Current time", action="store_true")
    parser.add_argument("-w", "--write", nargs=3, help="Write to file") # In fiture need to fixed nargs
    parser.add_argument("-r", "--read", nargs=2, help="Read to file") # this too fixed
    parser.add_argument("-ls", "--list", nargs="+", help="list the file")
    
    # for funny
    parser.add_argument("-os", "--typeos", action="store_true")

    return parser.parse_args()

def logic_arguments():
    """
    Функция где будут запускаться остальные функции по передачи аргументов от пользователя.
    """
    args = __initialization_arguments()
    
    if args.bubbleSort:
        lst_sort = bubble_algorithms(args.bubbleSort)
        print(lst_sort)
        write_a_to_file(fdata=str(lst_sort))
    elif args.time:
        print(current_time())
    elif args.write:
        write_a_to_file(fpath=args.write[0], fname=args.write[1], fdata=args.write[2],)
    elif args.read:
        print(reading_from_a_file(rpath=args.read[0], rname=args.read[1]))
    elif args.list:
        print(list_files(args.list[0], args.list[1]))
    elif args.typeos:
        feature_tip()


def removing_the_nesting_of_list(rlist=None):
    """
     Функция уберает ввложенные списки внутри списка, тем самым делая один полноценный
     список.
    """
    return sum(rlist, [])


def bubble_algorithms(numbers: int):

    """
     Алгоритм пузырьком. Просто, чтобы был.
    """

    lenght = len(numbers)

    for num in range(lenght - 1):
        for tnum in range(lenght - num - 1):
            if numbers[tnum] > numbers[tnum + 1]:
                numbers[tnum], numbers[tnum + 1] = numbers[tnum + 1], numbers[tnum]

    return numbers


def checking_directories():

    """
    Функция проверяет на наличии корневых обязательных папок, если их нет
    то функция возвращает False в противоположном случаие True.
    """

    root_folders = path.abspath("")
    root_dir = ('archive', 'main', 'management.py')

    for found in root_dir:
        if not found in listdir(root_folders):
            return False
    return True


def decorator_speed_measurement(func):

    """
    Декоратор для измерения скорости функции.
    """

    def speed_measurement_wrapper():
        start = time()
        func()
        print("Время исполнения функции - " + str(time() - start)[0:5] + " seconds")
        return func()
    return speed_measurement_wrapper


def current_time():

    """
    Функция выводить текущее время. Часы, минуты, секунды.
    """

    return datetime.now().strftime('%H:%M:%S')


def write_a_to_file(fdata=None, fpath=getcwd() + "/archive/", fname="files.txt", fmode="w", fencoding="utf-8"):

    """
    Функция записывает в данные в файл, аргументы функции будут перечислены.
    Аргументы:
        fpath - путь до файла
        fname - название файла
        fmode - мод записи файла
        fecoding - кодировка
        fdata - данные для записи в файл
    """

    try:
        with open(file=fpath + fname, mode=fmode, encoding=fencoding) as file:
            file.write(fdata)
    except TypeError as err:
        print(f"Ошибка:\n{err}")


def reading_from_a_file(lines= True, rpath=getcwd() + "/archive/", rname="files.txt", rmode="r"):

    """ 
    Функция читает данные из файла
    Возравщает строку или список из строк
    """

    try:
        if lines:
            with open(file=rpath + rname, mode=rmode) as rfile:
                data = rfile.readlines()
        else:
            with open(file=rpath + rname, mode=rmode) as rfile:
                data = rfile.readline().strip()
        return data

    except FileNotFoundError as err:
        print(f"Файл не найден:\n{err}")


def list_files(path, nfile = "*"):
    """
    Функция возвращает массив файлов
    """
    if path:
        return glob(f"{path}/{nfile}")
    else:
        return glob(f"{nfile}")



### ---------------------- ###
# Функции у которых нет логической цели в этой программе #
### ---------------------- ###



def feature_tip():
    """
     Бессмысленная функция, даёт совет по моему личному мнению. 
    """

    tuble_list = determining_the_operating_system()

    if tuble_list[1] == "Ты мой союзник!":
        print("Красавчик!")
    elif tuble_list[1] == "Мне Linux больше нравиться":
        print("https://ubuntu.com/")
    elif tuble_list[1] == "Бросай Windows, переходи на Linux!":
        print("https://ubuntu.com/")


def determining_the_operating_system():

    """
        Функция определяет операционную систему.
    """

    if platform == "linux" or platform == "linux2":
        return True, ("Ты мой союзник!")
    elif platform == "darwin":
        return True, ("Мне Linux больше нравиться, а тебе?")
    elif platform == "win32":
        return True, ("Бросай Windows, Переходи на линукс!")