import numpy as np
from queue import SimpleQueue

def is_path_clear(map, walls):
    grid_size = map['grid_size']
    start = tuple(map['agent_start_pos'])
    goal = tuple(map['goal_pos'])

    grid = np.zeros((grid_size, grid_size), dtype=int)
    for wall in walls:
        grid[wall[1], wall[0]] = 1  # Помечаем стены

    # Поиск в ширину (BFS)
    queue = SimpleQueue()
    queue.put(start)
    visited = set()
    visited.add(start)

    while not queue.empty():
        current = queue.get()
        if current == goal:
            return True
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in visited and grid[ny, nx] == 0:
                queue.put((nx, ny))
                visited.add((nx, ny))

    return False