import numpy as np
from queue import SimpleQueue

def is_path_clear(map_config, walls):
    grid_size = map_config['grid_size']
    start = tuple(map_config['agent_start_pos'])
    keys = [tuple(key[:2]) for key in map_config.get('keys', [])]  # Извлекаем координаты ключей

    # Создаем сетку
    grid = np.zeros((grid_size, grid_size), dtype=int)
    for wall in walls:
        x, y = wall
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y, x] = 1  # Помечаем стены

    def bfs(start_pos, target_pos):
        queue = SimpleQueue()
        queue.put(start_pos)
        visited = set()
        visited.add(start_pos)

        while not queue.empty():
            current = queue.get()
            if current == target_pos:
                return True
            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny, nx] == 0:
                    queue.put((nx, ny))
                    visited.add((nx, ny))

        return False

    # Проверяем путь через все ключи
    current_pos = start
    remaining_keys = keys.copy()

    while remaining_keys:
        # Проверяем, можно ли добраться до любого из оставшихся ключей
        reachable = False
        for key in remaining_keys:
            if bfs(current_pos, key):
                # Ключ доступен, перемещаемся к нему
                current_pos = key
                remaining_keys.remove(key)
                reachable = True
                break

        if not reachable:
            # Невозможно добраться до одного из ключей
            return False

    # Все ключи собраны
    return True