from utils.map_creation.map_creator_without_goal import MapCreator
from utils.map_creation.map_generator_without_goal import MapGenerator
from minimum_path import count_min_path_steps
from compare_decisions import compare_paths
from student_solution import solution
from info.print_map_info import print_map_info
from agent_movement import run_pygame

def process_paths(task_map, env):
    print_map_info(task_map)

    student_path = solution(task_map)
    min_steps, minimum_path = count_min_path_steps(task_map)
    if minimum_path is None:
        print("Минимальный путь не найден. Выход из программы.")
        return None, None

    comparison_result = compare_paths(student_path, task_map, min_steps)
    print("Минимальный путь:", minimum_path)
    print("Студенческий путь:", student_path)
    print("Сравнение путей:", comparison_result)

    run_pygame(env, student_path, task_map)

def start(config):
    task_map = MapGenerator().generate_random_map(config)
    env = MapCreator(task_map, render_mode="human")
    print(task_map)

    process_paths(task_map, env)
