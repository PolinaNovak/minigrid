from queue import PriorityQueue

from utils.path_control.a_star_search_return_path import heuristic

def a_star_search(grid_size, start, goal, walls):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            # Восстанавливаем путь
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return len(path) - 1, path  # Возвращаем длину пути и сам путь

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if not (0 <= neighbor[0] < grid_size and 0 <= neighbor[1] < grid_size):
                continue  # Выход за границы карты
            if neighbor in walls:
                continue  # Препятствие (стена)

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))

    return None, None  # Путь не найден

def count_min_path_steps(map):
    grid_size = map['grid_size']
    agent_pos = tuple(map['agent_start_pos'])
    walls = set(tuple(wall) for wall in map['walls'])
    keys = [(key[0], key[1]) for key in map['keys']]  # Извлекаем координаты ключей

    total_steps = 0
    full_path = []
    remaining_keys = set(keys)

    while remaining_keys:
        # Находим ближайший ключ
        closest_key = None
        closest_distance = float('inf')

        for key in remaining_keys:
            distance = heuristic(agent_pos, key)
            if distance < closest_distance:
                closest_key = key
                closest_distance = distance

        # Находим расстояние и путь до ближайшего ключа
        distance, path = a_star_search(grid_size, agent_pos, closest_key, walls)
        if distance is None:
            raise ValueError("Невозможно найти путь до ключа.")

        # Добавляем расстояние к общему количеству шагов
        total_steps += distance

        # Добавляем путь к полному пути
        if full_path:
            path = path[1:]
        full_path.extend(path)

        # Обновляем позицию агента и удаляем собранный ключ
        agent_pos = closest_key
        remaining_keys.remove(closest_key)

    return total_steps, full_path