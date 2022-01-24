import numpy as np
import pygame
import random
import os

from .Game import Game


class CatchGame(Game):
    
    def __init__(self):
        super().__init__(
            os.getenv('CATCH_NAME', 'Catch Game'),
            int(os.getenv('CATCH_GRID_WIDTH', 400)),
            int(os.getenv('CATCH_GRID_HEIGHT', 400))
        )
        self.BALL_WIDTH = 20
        self.BALL_HEIGHT = 20
        self.PADDLE_WIDTH = 50
        self.PADDLE_HEIGHT = 10
        self.GAME_FLOOR = 350
        self.GAME_CEILING = 10
        self.BALL_VELOCITY = 10
        self.PADDLE_VELOCITY = 20
        

    def reset(self):
        super().reset()
        self.paddle_x = self.GAME_WIDTH // 2
        self.ball_x = random.randint(0, self.GAME_WIDTH-20)
        self.ball_y = self.GAME_CEILING

    def execute_action(self, action):
        if action == self.LEFT:
            self.paddle_x -= self.PADDLE_VELOCITY
            if self.paddle_x < 0:
                self.paddle_x = self.PADDLE_VELOCITY
        elif action == self.RIGHT:
            self.paddle_x += self.PADDLE_VELOCITY
            if self.paddle_x > self.GAME_WIDTH - self.PADDLE_WIDTH:
                self.paddle_x = self.GAME_WIDTH - self.PADDLE_WIDTH - self.PADDLE_VELOCITY
        else:
            pass

    def update_screen_elements(self):
        self.ball_y += self.BALL_VELOCITY
        self.ball_position = pygame.draw.rect(self.screen, self.COLOR_WHITE,
                                pygame.Rect(self.ball_x, self.ball_y,
                                            self.BALL_WIDTH,
                                            self.BALL_HEIGHT))
        self.paddle_position = pygame.draw.rect(self.screen, self.COLOR_WHITE,
                                  pygame.Rect(self.paddle_x, 
                                              self.GAME_FLOOR,
                                              self.PADDLE_WIDTH,
                                              self.PADDLE_HEIGHT))

    def update_game_state(self):
        if self.has_colision():
            if self.catch_ball():
                self.current_reward = 1
                self.score = 10
            else:
                self.current_reward = -1

            self.ball_x = random.randint(0, self.GAME_WIDTH)
            self.ball_y = self.GAME_CEILING
            self.game_over = True
        self.current_frame = self.get_frame()

    def has_colision(self):
        return self.ball_y >= self.GAME_FLOOR - self.BALL_WIDTH // 2

    def catch_ball(self):
        return self.ball_position.colliderect(self.paddle_position)


if __name__ == "__main__":   
    game = CatchGame()

    NUM_EPOCHS = 2
    for e in range(NUM_EPOCHS):
        print(f"Epoch: {e}")
        game.reset()
        input_t = game.get_frame()
        game_over = False
        while not game_over:
            action = np.random.randint(0, 3, size=1)[0]
            input_tp1, reward, game_over, score = game.step(action)
            print(f"Action: {action}",
                f"Reward: {reward}",
                f"Game Over: {game_over}",
                f"Score: {score}")
