import pygame
from utils.control_agent_movement import calculate_direction, move_agent
from student_solution import solution
from map_update import update_walls_dynamically

def agent_step(env, next_pos):

    if next_pos is None:
        return False

    # Вычисляем направление и перемещаем агента
    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if env.agent_pos == env.goal_pos:
        return True

    return False

def run_pygame(env, map, config):
    max_steps = map.get('max_steps', 256)
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    total_steps = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if max_steps < total_steps:
            print("Лимит шагов исчерпан.")
            break

        next_step = solution(env, map)
        goal_reached = agent_step(env, next_step)

        if goal_reached:
            print("Успех! Вы добрались до финиша!")
            env.render()
            pygame.time.wait(2000)
            break

        map['agent_start_pos'] = list(next_step)
        map['walls'] = update_walls_dynamically(map, env, config['walls_update_per_second'])

        env.render()
        clock.tick(1)
        total_steps += 1

    pygame.quit()
