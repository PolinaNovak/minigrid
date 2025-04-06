def check_walls(task_map):
    grid_size = task_map['grid_size']
    walls = task_map.get('walls', [])
    walls_set = set(tuple(wall) for wall in walls)

    # Добавляем стены по краям, если их нет
    for x in range(grid_size):
        if (x, 0) not in walls_set:  # Верхняя граница
            task_map['walls'].append([x, 0])
        if (x, grid_size - 1) not in walls_set:  # Нижняя граница
            task_map['walls'].append([x, grid_size - 1])

    for y in range(1, grid_size - 1):  # Исключаем углы
        if (0, y) not in walls_set:  # Левая граница
            task_map['walls'].append([0, y])
        if (grid_size - 1, y) not in walls_set:  # Правая граница
            task_map['walls'].append([grid_size - 1, y])

    return task_map