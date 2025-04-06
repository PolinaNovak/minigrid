from utils.a_star_algorithm.a_star_search import a_star_search
from utils.a_star_algorithm.a_star_options import pathReturn, noneReturn

def find_optimal_path(task_map):
    grid_size = task_map['grid_size']
    start = tuple(task_map['agent_start_pos'])
    goal = tuple(task_map['goal_pos'])
    walls = set(map(tuple, task_map['walls']))

    return a_star_search(grid_size, start, goal, walls, pathReturn, noneReturn)

