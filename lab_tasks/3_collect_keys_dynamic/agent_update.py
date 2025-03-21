import random
from utils.path_control.a_star_search import a_star_search

def change_agent_position(map, env, remaining_keys):
    grid_size = map['grid_size']
    agent_pos = tuple(map['agent_start_pos'])
    walls = set(tuple(wall) for wall in map['walls'])
    attempts = 0
    max_attempts = 100

    while attempts < max_attempts:
        new_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

        # Проверяем, что новая позиция не содержит стену, ключ или агента
        if new_pos in walls or new_pos in remaining_keys or new_pos == agent_pos:
            attempts += 1
            continue

        # Проверяем, что из новой позиции можно достичь все оставшиеся ключи
        reachable = True
        for key in remaining_keys:
            if not a_star_search(grid_size, new_pos, key, walls):
                reachable = False
                break

        if reachable:
            # Обновляем позицию агента
            env.agent_pos = new_pos
            return new_pos

        attempts += 1

    raise ValueError("Не удалось найти подходящую позицию для агента после максимального количества попыток.")