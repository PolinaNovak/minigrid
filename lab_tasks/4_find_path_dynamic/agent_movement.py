import pygame
from utils.control_agent_movement import calculate_direction, move_agent
from student_solution import solution
from utils.map.map_update import update_walls_dynamically, add_walls_with_goal
from constants.marks import MARKS

def agent_step(env, next_pos):

    if next_pos is None:
        return False

    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if env.agent_pos == tuple(env.goal_pos):
        return True

    return False

def run_pygame(env, task_map, config):
    max_steps = task_map.get('max_steps', 256)
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    total_steps = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if max_steps < total_steps:
            print(
                f"Оценка: {MARKS['Не зачтено']}. Лимит шагов исчерпан. Выполнено шагов: {total_steps}, максимально допустимое: {max_steps}.")

            break

        next_step = solution(env, task_map)
        goal_reached = agent_step(env, next_step)
        if next_step is None:
            break

        if goal_reached:
            print(f"Оценка: {MARKS['Зачтено']}. Успех! Вы добрались до финиша!")
            env.render()
            pygame.time.wait(2000)
            break

        task_map['agent_start_pos'] = next_step
        task_map['walls'] = update_walls_dynamically(task_map, env, config, add_walls_with_goal)

        env.render()
        clock.tick(1)
        total_steps += 1

    pygame.quit()
