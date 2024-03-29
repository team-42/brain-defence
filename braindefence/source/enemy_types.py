from abc import abstractmethod

from pyglet import shapes


class EnemyType:
    def __init__(self, speed=180, max_health=5):
        self.speed = speed
        self.max_health = max_health

    @abstractmethod
    def drawable(self, x, y, batch):
        """
        Draws an enemy of this type.
        :param x: The x-coordinate where to draw.
        :param y: The y-coordinate where to draw.
        :param batch: The batch into which the enemy shall be drawn.
        :return: A drawable instance at the given position.
        """
        pass


class DefaultEnemy(EnemyType):
    def drawable(self, x, y, batch):
        return shapes.Circle(x=x, y=y, radius=10, color=(0, 0, 255), batch=batch)
