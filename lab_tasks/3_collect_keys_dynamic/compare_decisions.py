from constants.marks import MARKS
def compare_paths(student_path_length, max_steps, remaining_keys):

    if student_path_length > max_steps:
        return f"Ошибка: путь студента не является оптимальным. " \
               f"Количество шагов студента: {student_path_length}, максимально возможное количество шагов: {max_steps}." \
               f"Оценка: {MARKS['Хорошо']}"

    if len(remaining_keys) == 0:
        return (f"Успех! Все ключи собраны! Оценка: {MARKS['Отлично']}")
    else:
        return (f"Неудача. Не все ключи были собраны. Оценка: {MARKS['Удовлетворительно']}")

