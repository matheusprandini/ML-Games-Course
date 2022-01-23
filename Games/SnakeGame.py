import pygame, random
import collections
import numpy as np
import os

from pygame.locals import *

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

x = 1
y = 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

class SnakeGame():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake')
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_BLACK = (0, 0, 0)
        self.COLOR_GREEN = (25, 255, 0)
        self.COLOR_RED = (255,0,0)
        self.GAME_WIDTH = 200
        self.GAME_HEIGHT = 200
        self.reset()

    def execute_action(self, action):
        if action == LEFT and self.direction != RIGHT:
            self.direction = LEFT
        elif action == RIGHT and self.direction != LEFT:
            self.direction = RIGHT
        elif action == UP and self.direction != DOWN:
            self.direction = UP
        elif action == DOWN and self.direction != UP:
            self.direction = DOWN
        else:
            pass

    def update_snake_position(self):
        self.update_snake_tail_position()
        self.update_snake_head_position()

    def update_snake_head_position(self):
        if self.direction == UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
        elif self.direction == DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
        elif self.direction == RIGHT:
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])
        elif self.direction == LEFT:
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
        else:
            pass

    def update_snake_tail_position(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

    def update_screen_elements(self):
        self.screen.blit(self.apple, self.apple_pos)
        self.screen.blit(self.head_skin, self.snake[0])
        for i in range(1, len(self.snake)):
            self.screen.blit(self.tail_skin, self.snake[i])

        pygame.display.update()

    def update_game_state(self):
        if self.has_apple_collision():
            self.apple_pos = self.generate_random_position()
            self.snake.append((0,0))
            self.score += 10
            self.current_reward = 1

        if self.has_wall_colision() or self.has_head_and_tail_colision():
            self.game_over = True
            self.current_reward = -1

        self.current_frame = self.get_frame()

    def generate_random_position(self):
        x = random.randint(0,self.GAME_WIDTH - 10)
        y = random.randint(0,self.GAME_HEIGHT - 10)
        return (x//10 * 10, y//10 * 10)

    def has_apple_collision(self):
        return ((self.snake[0] == self.apple_pos[0]) and 
            (self.snake[1] == self.apple_pos[1]))

    def has_wall_colision(self):
        return (self.snake[0][0] < 0 or self.snake[0][1] < 0 or self.snake[0][0] > self.GAME_WIDTH - 10 or self.snake[0][1] > self.GAME_HEIGHT - 10)
    
    def has_head_and_tail_colision(self):
        return (len(self.snake) != len(set(self.snake)))

    def step(self, action):
        self.clock.tick(10)
        self.screen.fill(self.COLOR_BLACK)

        self.execute_action(action)
        self.update_snake_position()
        self.update_screen_elements()
        self.update_game_state()

        return self.current_frame, self.current_reward, self.game_over, self.score

    def get_frame(self):
        return pygame.surfarray.array3d(self.screen)
		
    def quit_game(self):
        pygame.quit()
		
    def reset(self):
        self.screen = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.clock = pygame.time.Clock()
		
        self.score = 0
        self.game_over = False
        self.current_reward = -0.01
        self.direction = LEFT
		
        self.snake = [(50, 50), (60, 50), (70,50)]
        self.head_skin = pygame.Surface((10,10))
        self.head_skin.fill(self.COLOR_GREEN)
        self.tail_skin = pygame.Surface((10,10))
        self.tail_skin.fill(self.COLOR_WHITE)
        
        self.apple_pos = self.generate_random_position()
        self.apple = pygame.Surface((10,10))
        self.apple.fill(self.COLOR_RED)
		
if __name__ == '__main__':
    game = SnakeGame()

    NUM_EPOCHS = 2
    for e in range(NUM_EPOCHS):
        print("Epoch: {:d}".format(e))
        game.reset()
        input_t = game.get_frame()
        game_over = False
        while not game_over:
            action = np.random.randint(0, 5, size=1)[0]
            input_tp1, current_reward, game_over, score = game.step(action)
            print(action, current_reward, game_over, score)