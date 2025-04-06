from utils.path_control.check_is_path_valid import is_valid_path
from constants.marks import MARKS
def compare_paths(optimal_path, student_path, task_map):
    grid_size = task_map['grid_size']
    wall_set = set(map(tuple, task_map['walls']))

    def reaches_goal(path, goal):
        return path[-1] == goal

    goal = optimal_path[-1]

    if not is_valid_path(student_path, wall_set, grid_size):
        return "Ошибка: путь студента выходит за границы карты или проходит через стены. " \
               "Либо при перемещении координаты изменяются более чем на 1. " \
               f"Оценка: {MARKS['Неудовлетворительно']}"

    if not reaches_goal(student_path, goal):
        return "Ошибка: путь студента не достигает цели. " \
               f"Оценка: {MARKS['Удовлетворительно']}"

    optimal_length = len(optimal_path)
    student_length = len(student_path)

    if student_path == optimal_path:
        return "Ответ студента полностью правильный! " \
               f"Оценка: {MARKS['Отлично']}"

    if student_length > optimal_length:
        return f"Ответ студента частично правильный. Длина пути студента: {student_length}, оптимальная длина: {optimal_length}. " \
               f"Оценка: {MARKS['Хорошо']}"

    if student_length < optimal_length:
        return f"Ответ студента полностью правильный! " \
               f"Оценка: {MARKS['Отлично']}"

    return "Путь не корректен. " \
           f"Оценка: {MARKS['Неудовлетворительно']}"
