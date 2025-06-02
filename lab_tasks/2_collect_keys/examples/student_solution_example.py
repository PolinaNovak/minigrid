from queue import PriorityQueue

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal, walls):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if not (0 <= neighbor[0] < grid and 0 <= neighbor[1] < grid):
                continue
            if neighbor in walls:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))

    return None
def solution(task_map):
    grid_size = task_map['grid_size']
    agent_pos = tuple(task_map['agent_start_pos'])
    walls = set(tuple(wall) for wall in task_map['walls'])
    keys = [(key[0], key[1]) for key in task_map['keys']]

    full_path = []
    remaining_keys = set(keys)

    while remaining_keys:
        closest_key = None
        closest_distance = float('inf')

        for key in remaining_keys:
            distance = heuristic(agent_pos, key)
            if distance < closest_distance:
                closest_key = key
                closest_distance = distance

        path = a_star_search(grid_size, agent_pos, closest_key, walls)
        if path is None:
            raise ValueError("Невозможно найти путь до ключа.")

        if full_path:
            path = path[1:]
        full_path.extend(path)

        agent_pos = closest_key
        remaining_keys.remove(closest_key)

    return full_path