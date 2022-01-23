# -*- coding: utf-8 -*-
from __future__ import division, print_function
import collections
import numpy as np
import pygame
import random
import os

x = 1
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

class CatchGame(object):
    
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(10, 100)

        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_BLACK = (0, 0, 0)
        self.GAME_WIDTH = 400
        self.GAME_HEIGHT = 400
        self.BALL_WIDTH = 20
        self.BALL_HEIGHT = 20
        self.PADDLE_WIDTH = 50
        self.PADDLE_HEIGHT = 10
        self.GAME_FLOOR = 350
        self.GAME_CEILING = 10
        self.BALL_VELOCITY = 10
        self.PADDLE_VELOCITY = 20
        

    def reset(self):
        self.screen = pygame.display.set_mode(
                (self.GAME_WIDTH, self.GAME_HEIGHT))
        self.clock = pygame.time.Clock()

        self.current_frame = self.get_frame()
        self.game_over = False
        self.paddle_x = self.GAME_WIDTH // 2
        self.reward = 0
        self.ball_x = random.randint(0, self.GAME_WIDTH-20)
        self.ball_y = self.GAME_CEILING

    def step(self, action):
        pygame.event.pump()
        self.screen.fill(self.COLOR_BLACK)

        self.execute_action(action)
        paddle_position = self.update_paddle_position()
        ball_position = self.update_ball_position()
        self.update_game_state(ball_position, paddle_position)

        pygame.display.flip()

        self.clock.tick(30)
        return self.current_frame, self.reward, self.game_over

    def execute_action(self, action):
        if action == 0:
            self.paddle_x -= self.PADDLE_VELOCITY
            if self.paddle_x < 0:
                self.paddle_x = self.PADDLE_VELOCITY
        elif action == 1:
            self.paddle_x += self.PADDLE_VELOCITY
            if self.paddle_x > self.GAME_WIDTH - self.PADDLE_WIDTH:
                self.paddle_x = self.GAME_WIDTH - self.PADDLE_WIDTH - self.PADDLE_VELOCITY
        else:
            pass

    def update_ball_position(self):
        self.ball_y += self.BALL_VELOCITY
        return pygame.draw.rect(self.screen, self.COLOR_WHITE,
                                pygame.Rect(self.ball_x, self.ball_y,
                                            self.BALL_WIDTH,
                                            self.BALL_HEIGHT))

    def update_paddle_position(self):
        return pygame.draw.rect(self.screen, self.COLOR_WHITE,
                                  pygame.Rect(self.paddle_x, 
                                              self.GAME_FLOOR,
                                              self.PADDLE_WIDTH,
                                              self.PADDLE_HEIGHT))

    def update_game_state(self, ball_position, paddle_position):
        if self.has_colision():
            if ball_position.colliderect(paddle_position):
                self.reward = 1
            else:
                self.reward = -1

            self.ball_x = random.randint(0, self.GAME_WIDTH)
            self.ball_y = self.GAME_CEILING
            self.game_over = True
        self.current_frame = self.get_frame()

    def has_colision(self):
        return self.ball_y >= self.GAME_FLOOR - self.BALL_WIDTH // 2

    def get_frame(self):
        return pygame.surfarray.array2d(self.screen)
    

if __name__ == "__main__":   
    game = CatchGame()

    NUM_EPOCHS = 10
    for e in range(NUM_EPOCHS):
        print("Epoch: {:d}".format(e))
        game.reset()
        input_t = game.get_frame()
        game_over = False
        while not game_over:
            action = np.random.randint(0, 3, size=1)[0]
            input_tp1, reward, game_over = game.step(action)
            print(action, reward, game_over)