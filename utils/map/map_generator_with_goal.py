import random
from utils.path_control.check_is_path_clear_with_goal import is_path_clear
from utils.check_walls import check_walls

class MapGenerator:
    def __init__(self):
        pass

    def generate_random_map(self, config):

        if "seed" in config:
            random.seed(config["seed"])

        max_attempts = config.get("max_attempts", 100)
        attempts = 0

        while attempts < max_attempts:
            attempts += 1

            if "map" in config:
                predefined_map = check_walls(config["map"])

                if not is_path_clear(predefined_map, predefined_map.get('walls', [])):
                    raise ValueError("Заданная карта является непроходимой.")
                return predefined_map

            grid_min_size = config.get("min_size", 5)
            grid_max_size = config.get("max_size", 20)
            grid_size = random.randint(grid_min_size, grid_max_size)
            agent_start_pos = (random.randint(1, grid_size - 2), random.randint(1, grid_size - 2))
            goal_pos = (random.randint(1, grid_size - 2), random.randint(1, grid_size - 2))

            while agent_start_pos == goal_pos:
                goal_pos = (random.randint(1, grid_size - 2), random.randint(1, grid_size - 2))

            generated_map = {
                'grid_size': grid_size,
                'agent_start_pos': list(agent_start_pos),
                'agent_start_dir': 0,
                'max_steps': grid_size * grid_size * 4,
                'goal_pos': tuple(goal_pos),
                'walls': [],
                'doors': [],
                'keys': [],
                'task_name': config.get("task_name", "")
            }

            for x in range(grid_size):
                generated_map['walls'].append([x, 0])
                generated_map['walls'].append([x, grid_size - 1])
            for y in range(grid_size):
                generated_map['walls'].append([0, y])
                generated_map['walls'].append([grid_size - 1, y])

            num_walls = int(grid_size * grid_size * config.get("wall_density", 0.3))
            for _ in range(num_walls):
                while True:
                    x, y = random.randint(1, grid_size - 2), random.randint(1, grid_size - 2)
                    if [x, y] in generated_map['walls'] or (x, y) == agent_start_pos or (x, y) == goal_pos:
                        continue
                    generated_map['walls'].append([x, y])
                    break

            if is_path_clear(generated_map, generated_map['walls']):
                return generated_map

        raise RuntimeError(f"Не удалось сгенерировать проходимую карту после {max_attempts} попыток.")


