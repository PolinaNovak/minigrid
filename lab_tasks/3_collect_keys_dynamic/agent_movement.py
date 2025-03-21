import pygame
import time
from utils.control_agent_movement import calculate_direction, move_agent
from student_solution import solution
from map_update import update_walls_dynamically
from compare_decisions import compare_paths
from agent_update import change_agent_position


def agent_step(env, next_pos, remaining_keys, map):
    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if next_pos in remaining_keys:
        x, y = next_pos
        # Удаляем ключ из сетки
        if env.grid.get(x, y) and env.grid.get(x, y).type == "key":
            env.grid.set(x, y, None)
            remaining_keys.remove(next_pos)
            print(f"Ключ собран! Осталось собрать: {len(remaining_keys)}")
            env.render()
            time.sleep(1)
            return change_agent_position(map, env, remaining_keys)

    return next_pos


def run_pygame(env, map, config):
    keys = [(key[0], key[1]) for key in map['keys']]
    max_steps = map.get('max_steps', 256)

    pygame.init()
    clock = pygame.time.Clock()

    running = True
    total_steps = 0

    # Инициализация оставшихся ключей
    remaining_keys = set(tuple(key[:2]) for key in keys)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if max_steps < total_steps:
            print("Лимит шагов исчерпан.")
            break

        next_step = solution(map, remaining_keys)
        if next_step is None:
            break

        next_step = agent_step(env, next_step, remaining_keys, map)
        map['agent_start_pos'] = next_step

        map['walls'] = update_walls_dynamically(map, env, config['walls_update_per_second'])

        env.render()
        clock.tick(1)
        total_steps += 1

    comparison_result = compare_paths(total_steps, max_steps, remaining_keys)
    print("Результат программы:", comparison_result)

    pygame.quit()
