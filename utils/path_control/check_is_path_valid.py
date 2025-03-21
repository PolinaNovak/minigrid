def is_valid_path(path, wall_set, grid_size):
    for i, (x, y) in enumerate(path):

        if not (0 <= x < grid_size and 0 <= y < grid_size):
            return False  # Координаты вне границ карты

        if (x, y) in wall_set:
            return False  # Путь проходит через стену

        if i > 0:
            prev_x, prev_y = path[i - 1]
            dx, dy = abs(x - prev_x), abs(y - prev_y)
            if dx > 1 or dy > 1 or (dx == 0 and dy == 0):
                return False  # Недопустимое перемещение

    return True