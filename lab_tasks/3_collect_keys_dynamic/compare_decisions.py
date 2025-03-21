def compare_paths(student_path_length, max_steps, remaining_keys):

    if student_path_length > max_steps:
        return f"Ошибка: путь студента не является оптимальным. " \
               f"Количество шагов студента: {student_path_length}, максимально возможное количество шагов: {max_steps}."

    if len(remaining_keys) == 0:
        return ("Успех! Все ключи собраны!")
    else:
        return ("Неудача. Не все ключи были собраны.")

