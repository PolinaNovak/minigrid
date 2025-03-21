def print_map_info(task_map):
    grid_size = task_map.get("grid_size", "Неизвестно")
    start = task_map.get("agent_start_pos", "Неизвестно")
    goal = task_map.get("goal_pos", "Неизвестно")
    walls = task_map.get("walls", [])

    print("\n=== Информация о карте ===")
    print(f"Размер сетки: {grid_size}x{grid_size}")
    print(f"Начальная позиция агента: {start}")
    print(f"Целевая позиция: {goal}")
    print(f"Количество стен: {len(walls)}")
    if walls:
        print_wall_map(task_map)
    else:
        print("На карте нет стен.")


def print_wall_map(task_map):
    grid_size = task_map.get("grid_size", 10)
    walls = task_map.get("walls", [])

    wall_map = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    for wall in walls:
        x, y = wall
        if 0 <= x < grid_size and 0 <= y < grid_size:
            wall_map[x][y] = 1

    print("\n=== Карта стен ===")
    for row in wall_map:
        print(" ".join(map(str, row)))
    print("\n")