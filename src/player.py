import time
from image_dict import IMAGEDICT
from point import Point 

class Player:
    def __init__(self, image_key, x, y):
        self.image = IMAGEDICT[image_key]
        self.position = Point(x, y)
        self.y_velocity = 0
        self.size = 50
        self.on_ground = True
        self.gravity = 0.5
        self.jump_height = -5
        self.start_time = time.time()
        self.jump_delay = 0.5

    def jump(self):
        self.y_velocity += self.jump_height
        self.on_ground = False

    def update(self, height_limit):
        self.y_velocity += self.gravity
        self.position.y += self.y_velocity

        if self.position.y >= height_limit - self.size:
            self.position.y = height_limit - self.size
            self.on_ground = True
            self.y_velocity = 0