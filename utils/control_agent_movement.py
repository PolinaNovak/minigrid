from constants.direction import DIRECTIONS
import pygame
def calculate_direction(current_pos, next_pos):
    dx = next_pos[0] - current_pos[0]
    dy = next_pos[1] - current_pos[1]
    return DIRECTIONS.get((dx, dy))


def move_agent(env, new_pos, direction):
    env.agent_dir = direction
    pygame.time.wait(100)
    env.agent_pos = new_pos
