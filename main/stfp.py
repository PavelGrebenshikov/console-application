from .functions import checking_directories, logic_arguments

def started_program():

    # Проверка на наличия необходимых директорий в проекте
    if checking_directories():
        logic_arguments()
    else:
        print(f"Была не найдена директория: ['archive', 'main', management.py]")
