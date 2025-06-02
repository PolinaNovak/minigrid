from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Goal, Wall, Door, Key
from minigrid.minigrid_env import MiniGridEnv

class MapCreator(MiniGridEnv):
    def __init__(
            self,
            config,
            **kwargs,
    ):
        self.size = config['grid_size']
        self.agent_start_pos = config['agent_start_pos']
        self.agent_start_dir = config['agent_start_dir']
        self.goal_pos = config['goal_pos']
        self.max_steps = config['max_steps']
        self.walls = config['walls']
        self.doors = config['doors']
        self.keys = config['keys']
        self.agent_pos = self.agent_start_pos
        self.task_name = config.get('task_name', "")

        if config['walls'] is None:
            self.walls = []

        if config['doors'] is None:
            self.doors = []

        if config['keys'] is None:
            self.keys = []

        mission_space = MissionSpace(mission_func=lambda: self.task_name)

        super().__init__(
            mission_space=mission_space,
            grid_size=self.size,
            see_through_walls=True,
            max_steps=self.max_steps,
            **kwargs,
        )

        self.step_count = 0
        self.steps_counter = 0
        self.agent_has_key = []
        self._gen_grid(self.size, self.size)

    def get_cell(self, x, y):
        if not (0 <= x < self.grid.width and 0 <= y < self.grid.height):
            return None

        cell = self.grid.get(x, y)
        return cell


    def create_walls(self):
        for wall_coords in self.walls:
            x_wall, y_wall = wall_coords
            self.grid.set(x_wall, y_wall, Wall())

    def create_doors(self):
        for door_coords in self.doors:
            x_door, y_door, color_door = door_coords
            self.grid.set(x_door, y_door, Door(color=color_door, is_locked='true'))
            self.grid.get(x_door, y_door).can_overlap()

    def create_keys(self):
        for key_coords in self.keys:
            x_door, y_door, color_key = key_coords
            self.grid.set(x_door, y_door, Key(color=color_key))

    def _gen_grid(self, width, height):
        self.grid = Grid(width, height)

        self.grid.wall_rect(0, 0, width, height)

        self.create_walls()

        self.create_doors()

        self.create_keys()

        self.put_obj(Goal(), *self.goal_pos)

        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

    def get_grid_map(self):
        if self.grid is None:
            return []
        return self.grid.encode()[:, :, 0].T

    def get_image_map(self):
        prev_render = self.render_mode
        self.render_mode = 'rgb_array'
        image = self.render()
        self.render_mode = prev_render
        self.render()
        return image

    def get_grid(self):
        return self.grid

    def get_actor_pos(self):
        return self.agent_pos

