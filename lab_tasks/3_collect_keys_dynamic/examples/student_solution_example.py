
from queue import PriorityQueue

from utils.path_control.a_star_search import heuristic

def a_star_search(grid_size, start, goal, walls):
    if isinstance(grid_size, int):
        grid_size = (grid_size, grid_size)

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
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Проверяем выход за границы карты
            if not (0 <= neighbor[0] < grid_size[0] and 0 <= neighbor[1] < grid_size[1]):
                continue
            if neighbor in walls:
                continue  # Препятствие (стена)

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))

    return None  # Путь не найден


def solution(map, remaining_keys):
    grid_size = map['grid_size']
    agent_pos = tuple(map['agent_start_pos'])
    walls = set(tuple(wall) for wall in map['walls'])

    # Находим ближайший ключ
    closest_key = None
    closest_distance = float('inf')

    for key in remaining_keys:
        distance = heuristic(agent_pos, key)
        if distance < closest_distance:
            closest_key = key
            closest_distance = distance

    if closest_key is None:
        return None  # Нет доступных ключей

    # Ищем путь до ближайшего ключа
    path = a_star_search(grid_size, agent_pos, closest_key, walls)
    if path is None or len(path) < 2:
        return None

    return path[1]

