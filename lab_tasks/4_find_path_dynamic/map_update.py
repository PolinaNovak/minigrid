import random

from minigrid import Wall

from utils.path_control.check_is_path_clear_with_goal import is_path_clear

def remove_walls(env, walls, walls_to_remove_count):
    removed_walls = []
    for _ in range(walls_to_remove_count):
        if not walls:
            break
        wall_to_remove = random.choice(list(walls))
        env.grid.set(wall_to_remove[0], wall_to_remove[1], None)  # Удаляем стену с карты
        removed_walls.append(wall_to_remove)
        walls.remove(wall_to_remove)
    return walls

def add_walls(env, map, walls_to_add_count):
    grid_size = map['grid_size']
    walls = set(tuple(wall) for wall in map['walls'])
    agent_pos = tuple(map['agent_start_pos'])
    goal_pos = tuple(map['goal_pos'])

    added_walls = []
    attempts = 0
    max_attempts = 100

    while walls_to_add_count > 0 and attempts < max_attempts:
        new_wall = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))

        if new_wall == agent_pos or new_wall == goal_pos or new_wall in walls:
            attempts += 1
            continue

        # Проверяем, что карта остаётся проходимой
        temp_walls = walls.copy()
        temp_walls.add(new_wall)
        if is_path_clear(map, temp_walls):
            walls.add(new_wall)
            env.grid.set(new_wall[0], new_wall[1], Wall())  # Добавляем стену на карту
            added_walls.append(new_wall)
            walls_to_add_count -= 1

        attempts += 1

    return walls

def update_walls_dynamically(map, env, walls_update_per_second=5):
    walls = set(tuple(wall) for wall in map['walls'])

    # Удаление стен
    walls_to_remove_count = min(walls_update_per_second, len(walls))
    walls = remove_walls(env, walls, walls_to_remove_count)

    # Добавление стен
    walls = add_walls(env, map, walls_to_remove_count)

    # Обновляем конфигурацию карты
    return walls
