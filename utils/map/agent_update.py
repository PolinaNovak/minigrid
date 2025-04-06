import random
from utils.a_star_algorithm.a_star_search import a_star_search
from utils.a_star_algorithm.a_star_options import booleanTrueReturn, booleanFalseReturn
def change_agent_position_with_keys(task_map, env, remaining_keys):
    grid_size = task_map['grid_size']
    agent_pos = tuple(task_map['agent_start_pos'])
    walls = set(tuple(wall) for wall in task_map['walls'])
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
            if not a_star_search(grid_size, new_pos, key, walls, booleanTrueReturn, booleanFalseReturn):
                reachable = False
                break

        if reachable:
            # Обновляем позицию агента
            env.agent_pos = new_pos
            return new_pos

        attempts += 1

    raise ValueError("Не удалось найти подходящую позицию для агента после максимального количества попыток.")




def change_agent_position_with_goal(task_map, env):
    grid_size = task_map['grid_size']
    agent_pos = tuple(task_map['agent_start_pos'])
    walls = set(tuple(wall) for wall in task_map['walls'])
    goal_pos = tuple(task_map['goal_pos'])
    attempts = 0
    max_attempts = 100

    while attempts < max_attempts:
        new_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

        # Проверяем, что новая позиция не содержит стену, ключ или агента
        if new_pos in walls or new_pos == goal_pos or new_pos == agent_pos:
            attempts += 1
            continue

        # Проверяем, что из новой позиции можно достичь все оставшиеся ключи
        if a_star_search(grid_size, new_pos, goal_pos, walls, booleanTrueReturn, booleanFalseReturn):
            env.agent_pos = new_pos
            return new_pos

        attempts += 1

    raise ValueError("Не удалось найти подходящую позицию для агента после максимального количества попыток.")