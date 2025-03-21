import pygame
from utils.control_agent_movement import calculate_direction, move_agent

def agent_step(env, next_pos):
    # Вычисляем направление и перемещаем агента
    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if env.agent_pos == env.goal_pos:
        return True

    return False

def run_pygame(env, student_path, goal):
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    current_step = 1
    total_steps = len(student_path)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_step >= total_steps:
            print("Все шаги выполнены.")
            break

        next_pos = student_path[current_step]
        goal_reached = agent_step(env, next_pos)
        if goal_reached:
            env.render()
            pygame.time.wait(2000)
            break

        env.render()
        clock.tick(1)
        current_step += 1

    pygame.quit()
