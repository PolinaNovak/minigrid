import pygame
from utils.control_agent_movement import calculate_direction, move_agent
from constants.marks import MARKS
def agent_step(env, next_pos, remaining_keys):
    direction = calculate_direction(env.agent_pos, next_pos)
    if direction is not None:
        move_agent(env, next_pos, direction)

    if next_pos in remaining_keys:
        x, y = next_pos
        if env.grid.get(x, y) and env.grid.get(x, y).type == "key":
            env.grid.set(x, y, None)
            remaining_keys.remove(next_pos)
            print(f"Ключ собран! Осталось собрать: {len(remaining_keys)}")
            return True

    return False

def run_pygame(env, student_path, task_map):
    keys = [(key[0], key[1]) for key in task_map['keys']]
    pygame.init()
    clock = pygame.time.Clock()

    running = True
    current_step = 0
    total_steps = len(student_path)

    remaining_keys = set(tuple(key[:2]) for key in keys)
    collected_keys = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_step >= total_steps:
            print(f"Лимит шагов исчерпан. Оценка: {MARKS['Неудовлетворительно']}")
            break

        next_pos = student_path[current_step]

        key_collected = agent_step(env, next_pos, remaining_keys)
        if key_collected:
            collected_keys += 1

        env.render()
        clock.tick(1)
        current_step += 1

    if len(remaining_keys) == 0:
        print(f"Успех! Все ключи собраны!")
    else:
        print(f"Неудача. Не все ключи были собраны.")

    pygame.quit()
