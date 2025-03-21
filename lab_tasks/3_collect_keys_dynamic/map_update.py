import random
def update_walls_dynamically(map, env, walls_update_per_second=5):
    walls = set(tuple(wall) for wall in map['walls'])
    walls_to_remove_count = min(walls_update_per_second, len(walls) - 5)

    if walls_to_remove_count > 0:
        for _ in range(walls_update_per_second):
            wall_to_remove = random.choice(list(walls))
            env.grid.set(wall_to_remove[0], wall_to_remove[1], None)
            walls.remove(wall_to_remove)

    return walls
