import pygame
import time
from utils.control_agent_movement import calculate_direction, move_agent
from student_solution import solution
from utils.map.map_update import update_walls_dynamically, add_walls_with_keys
from compare_decisions import compare_paths
from utils.map.agent_update import change_agent_position_with_keys
from constants.marks import MARKS

def agent_step(env, next_pos, remaining_keys, task_map, is_teleportating):
    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if next_pos in remaining_keys:
        x, y = next_pos
        if env.grid.get(x, y) and env.grid.get(x, y).type == "key":
            env.grid.set(x, y, None)
            remaining_keys.remove(next_pos)
            print(f"Ключ собран! Осталось собрать: {len(remaining_keys)}")
            env.render()
            time.sleep(1)
            if is_teleportating:
                return list(change_agent_position_with_keys(task_map, env, remaining_keys)), remaining_keys

    return list(next_pos), remaining_keys


def run_pygame(env, task_map, config):
    keys = [(key[0], key[1]) for key in task_map['keys']]
    max_steps = task_map.get('max_steps', 256)
    agent_teleportation = False

    if "dynamic" in config:
        agent_teleportation = config.get('agent_teleportation', False)

    pygame.init()
    clock = pygame.time.Clock()

    running = True
    total_steps = 0

    remaining_keys = set(tuple(key[:2]) for key in keys)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if max_steps < total_steps:
            print(f"Лимит шагов исчерпан. Оценка: {MARKS['Неудовлетворительно']}")
            break

        next_step= solution(task_map, remaining_keys)
        if next_step is None:
            break

        next_step, task_map['keys'] = agent_step(env, next_step, remaining_keys, task_map, agent_teleportation)
        task_map['agent_start_pos'] = next_step

        task_map['walls'] = update_walls_dynamically(task_map, env, config,
                                                     add_walls_with_keys)

        env.render()
        clock.tick(1)
        total_steps += 1

    comparison_result = compare_paths(total_steps, max_steps, remaining_keys)
    print("Результат программы:", comparison_result)

    pygame.quit()
