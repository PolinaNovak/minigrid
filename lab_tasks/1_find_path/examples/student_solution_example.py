from queue import PriorityQueue

def is_passable(x, y, env, grid_size):

    if not (0 <= x < grid_size and 0 <= y < grid_size):
        return False

    # Проверяем состояние клетки
    cell = env.get_cell(x, y)  # Предполагаем, что у среды есть метод get_cell
    if (cell is None):
        return True
    if cell.type == "wall":  # Если клетка занята стеной
        return False
    if cell.type == "obstacle":  # Если клетка занята другим препятствием
        return False

    return True


def solution(current_pos, goal, env, grid_size):

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = PriorityQueue()
    open_set.put((0, current_pos))
    came_from = {}
    cost_so_far = {current_pos: 0}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = []
            while current != current_pos:
                path.append(current)
                current = came_from[current]
            path.append(current_pos)
            path.reverse()
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            # Проверяем проходимость и игнорируем уже проверенные
            if not is_passable(*neighbor, env, grid_size):
                continue

            new_cost = cost_so_far[current] + 1  # Стоимость перехода между соседями = 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                open_set.put((priority, neighbor))
                came_from[neighbor] = current

    return []
