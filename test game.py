import unittest
import pygame
import random
import os

class TestCarGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.mixer.init()

        self.size = width, height = (1200, 800)
        self.road_w = int(width/1.6)
        self.roadmark_w = int(width/60)
        self.right_lane = width/2 + self.road_w/4
        self.left_lane = width/2 - self.road_w/4

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('warm.mp3')
        self.sound.set_volume(0.5)
        self.score = 0

        self.running = True
        self.screen = pygame.display.set_mode((self.size))
        pygame.display.set_caption("Sangay's car game")
        self.screen.fill((60, 220, 0))

        self.car = pygame.image.load("car.png")
        self.car_loc = self.car.get_rect()
        self.car_loc.center = width/3 + self.road_w/2, height*0.7

        self.car2 = pygame.image.load("car2.png")
        self.car2_loc = self.car2.get_rect()
        self.car2_loc.center = self.left_lane, height*0.2

    def test_collision_detection(self):
        # Simulate a collision
        self.car_loc.center = self.left_lane, self.car2_loc.centery
        self.assertTrue(self.car_loc.colliderect(self.car2_loc))

        # Simulate no collision
        self.car_loc.center = self.right_lane, self.car2_loc.centery - 100
        self.assertFalse(self.car_loc.colliderect(self.car2_loc))

    def test_enemy_vehicle_movement(self):
        initial_y = self.car2_loc.y

        # Simulate the game loop to make the enemy vehicle move
        for _ in range(100):
            self.car2_loc.y += 3
            if self.car2_loc.y > self.size[1]:
                if random.randint(0, 1) == 0:
                    self.car2_loc.center = self.right_lane, -200
                else:
                    self.car2_loc.center = self.left_lane, -200

        # Check if the enemy vehicle has moved
        self.assertNotEqual(initial_y, self.car2_loc.y)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
