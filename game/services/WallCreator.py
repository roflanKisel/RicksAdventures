from game.entities.barriers.Barrier import Barrier


class WallCreator:
    @staticmethod
    def create_horizontal_walls(image, start_position, number, wall_type='wall'):
        walls = []
        if wall_type == 'spine':
            for _ in range(number):
                wall = Barrier(image, tuple(start_position), True)
                walls.append(wall)
                start_position[0] += (wall.width - 1)
        else:
            for _ in range(number):
                wall = Barrier(image, tuple(start_position), False)
                walls.append(wall)
                start_position[0] += (wall.width - 1)
        return walls

    @staticmethod
    def create_vertical_walls(image, start_position, number, wall_type='wall'):
        walls = []
        if wall_type == 'spine':
            for _ in range(number):
                wall = Barrier(image, tuple(start_position), True)
                walls.append(wall)
                start_position[1] += (wall.height - 1)
        else:
            for _ in range(number):
                wall = Barrier(image, tuple(start_position), False)
                walls.append(wall)
                start_position[1] += (wall.height - 1)
        return walls
