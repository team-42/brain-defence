import arcade
from arcade import Texture

from braindefence import RESOURCE_DIR
from braindefence.arcade.entities import Entity
from braindefence.arcade.constants import World


class Impression(Entity):
    def __init__(
        self, impressionWaypoints, startPoint, imagefilepath, character_scaling
    ):
        # Setup parent class
        super().__init__(imagefilepath, character_scaling)
        self.textures = [
            arcade.load_texture(RESOURCE_DIR.joinpath("impressions/impression-1.png").resolve()),
            arcade.load_texture(RESOURCE_DIR.joinpath("impressions/impression-1-good.png").resolve()),
            arcade.load_texture(RESOURCE_DIR.joinpath("impressions/impression-1-bad.png").resolve())
            ]
        self.set_texture(2)
        self._atDestination = False
        self.impressionWaypoints = impressionWaypoints
        self.maxPositiveHealth = 0
        self.maxNegativeHealth = -30
        self.currentHealth = -30
        self.speed = 300
        self._targetX = impressionWaypoints[0][0]
        self._targetY = impressionWaypoints[0][1]
        self.atWayPoint = 0

        self.center_x = startPoint[0]
        self.center_y = startPoint[1]
        self.hit_box = [[-10, -10], [-10, 10], [10, 10], [10, -10]]

    def update(self, dt):
        # print("Current Target: ", self._targetX, self._targetY, "Position: ", self.center_x, self.center_y)
        delta_x = self._targetX - self.center_x
        delta_y = self._targetY - self.center_y
        self.center_x += (delta_x * self.speed * dt) / (abs(delta_x) + abs(delta_y))
        self.center_y += (delta_y * self.speed * dt) / (abs(delta_x) + abs(delta_y))

        if self.collides_with_point([self._targetX, self._targetY]):
            self.atWayPoint += 1
            # print(self.atWayPoint, len(self.impressionWaypoints) - 1)
            if self.atWayPoint > len(self.impressionWaypoints) - 1:
                self._atDestination = True
            else:
                self._targetX = self.impressionWaypoints[self.atWayPoint][0]
                self._targetY = self.impressionWaypoints[self.atWayPoint][1]

    def passed(self):
        return self._atDestination

    def hit_by(self, projectile):
        self.currentHealth = min(self.maxPositiveHealth, self.currentHealth + projectile.damage)
        if self.currentHealth > self.maxPositiveHealth * 0.4:
            self.set_texture(1)
        elif self.currentHealth < self.maxNegativeHealth * 0.4:
            self.set_texture(2)
        else:
            self.set_texture(0)

