from utils.map.map_creator_with_goal import MapCreator
from utils.map.map_generator_with_goal import MapGenerator
from optimal_path import find_optimal_path
from compare_decisions import compare_paths
from student_solution import solution
from info.print_map_info import print_map_info
from agent_movement import run_pygame

def process_paths(task_map, env):
    print_map_info(task_map)

    student_path = solution(task_map, env)
    optimal_path = find_optimal_path(task_map)
    if optimal_path is None:
        print("Оптимальный путь не найден. Выход из программы.")
        return None, None

    comparison_result = compare_paths(optimal_path, student_path, task_map)
    print("Оптимальный путь:", optimal_path)
    print("Студенческий путь:", student_path)
    print("Сравнение путей:", comparison_result)

    run_pygame(env, student_path)

    return optimal_path, student_path

def start(config):
    task_map = MapGenerator().generate_random_map(config)
    env = MapCreator(task_map, render_mode="human")

    process_paths(task_map, env)
