from utils.path_control.check_is_path_valid import is_valid_path
from constants.marks import MARKS
def compare_paths(student_path, task_map, min_steps):
    grid_size = task_map['grid_size']
    walls = set(tuple(wall) for wall in task_map['walls'])

    if not is_valid_path(student_path, walls, grid_size):
        return "Ошибка: путь студента выходит за границы карты или проходит через стены. " \
               "Либо при перемещении координаты изменяются более чем на 1. " \
               f"Оценка: {MARKS['Неудовлетворительно']}"

    student_length = len(student_path) - 1
    if student_length > min_steps:
        return f"Ошибка: путь студента не является оптимальным. " \
               f"Длина пути студента: {student_length}, минимальная длина: {min_steps}. " \
               f"Оценка: {MARKS['Хорошо']}"

    if student_length == min_steps:
        return "Ответ студента полностью правильный! " \
               f"Оценка: {MARKS['Отлично']}"

    return f"Путь не корректен. Оценка: {MARKS['Неудовлетворительно']}"
