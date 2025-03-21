from utils.map_creation.map_creator_with_goal import MapCreator
from utils.map_creation.map_generator_with_goal import MapGenerator
from info.print_map_info import print_map_info
from agent_movement import run_pygame

def process_paths(task_map, env, config):
    print_map_info(task_map)

    run_pygame(env, task_map, config)


def start(config):
    task_map = MapGenerator().generate_random_map(config)
    env = MapCreator(task_map, render_mode="human")
    print(task_map['goal_pos'])

    process_paths(task_map, env, config)
