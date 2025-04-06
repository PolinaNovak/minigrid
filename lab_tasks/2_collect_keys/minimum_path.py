from utils.a_star_algorithm.a_star_search import a_star_search
from utils.a_star_algorithm.heuristic import heuristic
from utils.a_star_algorithm.a_star_options import lengthAndPathReturn, noneNoneReturn


def count_min_path_steps(task_map):
    grid_size = task_map['grid_size']
    agent_pos = tuple(task_map['agent_start_pos'])
    walls = set(tuple(wall) for wall in task_map['walls'])
    keys = [(key[0], key[1]) for key in task_map['keys']]  # Извлекаем координаты ключей

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
        distance, path = a_star_search(grid_size, agent_pos, closest_key, walls, lengthAndPathReturn, noneNoneReturn)
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
