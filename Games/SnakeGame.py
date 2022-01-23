import pygame, random
import numpy as np

from pygame.locals import *

from Game import Game


class SnakeGame(Game):

    def __init__(self):
        super().__init__('Snake', 200, 200)

    def reset(self):
        super().reset()

        self.direction = self.LEFT
		
        self.snake = [(50, 50), (60, 50), (70,50)]
        self.head_skin = pygame.Surface((10,10))
        self.head_skin.fill(self.COLOR_GREEN)
        self.tail_skin = pygame.Surface((10,10))
        self.tail_skin.fill(self.COLOR_WHITE)
        
        self.apple_pos = self.generate_random_position()
        self.apple = pygame.Surface((10,10))
        self.apple.fill(self.COLOR_RED)

    def execute_action(self, action):
        if action == self.LEFT and self.direction != self.RIGHT:
            self.direction = self.LEFT
        elif action == self.RIGHT and self.direction != self.LEFT:
            self.direction = self.RIGHT
        elif action == self.UP and self.direction != self.DOWN:
            self.direction = self.UP
        elif action == self.DOWN and self.direction != self.UP:
            self.direction = self.DOWN
        else:
            pass

    def update_screen_elements(self):
        self.update_snake_tail_position()
        self.update_snake_head_position()
        self.update_element_colors()

    def update_snake_head_position(self):
        if self.direction == self.UP:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - 10)
        elif self.direction == self.DOWN:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + 10)
        elif self.direction == self.RIGHT:
            self.snake[0] = (self.snake[0][0] + 10, self.snake[0][1])
        elif self.direction == self.LEFT:
            self.snake[0] = (self.snake[0][0] - 10, self.snake[0][1])
        else:
            pass

    def update_snake_tail_position(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i-1][0], self.snake[i-1][1])

    def update_element_colors(self):
        self.screen.blit(self.apple, self.apple_pos)
        self.screen.blit(self.head_skin, self.snake[0])
        for i in range(1, len(self.snake)):
            self.screen.blit(self.tail_skin, self.snake[i])

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
            input_tp1, reward, game_over, score = game.step(action)
            print(f"Action: {action}",
                f"Reward: {reward}",
                f"Game Over: {game_over}",
                f"Score: {score}")
