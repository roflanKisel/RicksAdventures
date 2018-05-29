from cocos import actions
from pyglet.window import key
from config.config import keyboard
from game.entities.barriers.Barrier import Barrier
from config.config import collision_manager


class ActionController(actions.Action):
    MOVE_SPEED = 200

    def start(self):
        self.target.velocity = (0, 0)

    def step(self, dt):
        if dt > 0.1:
            # a too big dt will move the player through walls
            # dt can be big at startup in slow hardware
            return

        vx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * self.MOVE_SPEED
        vy = (keyboard[key.UP] - keyboard[key.DOWN]) * self.MOVE_SPEED

        # with the updated velocity calculate the (tentative) displacement
        dx = vx * dt
        dy = vy * dt

        # get the player's current bounding rectangle
        last = self.target.get_rect()
        new = last.copy()
        new.x += dx
        new.y += dy

        self.target.position = new.center
        collisions = collision_manager.objs_colliding(self.target)

        # collision with wall handler
        if ActionController.__is_barrier_in_collisions(collisions):
            print(collisions)

            keyboard.clear()
            last.x -= dx
            last.y -= dy
            self.target.position = last.center

    @staticmethod
    def __is_barrier_in_collisions(collisions):
        for collision in collisions:
            if isinstance(collision, Barrier):
                if not collision.is_damaging:
                    return True
        return False
