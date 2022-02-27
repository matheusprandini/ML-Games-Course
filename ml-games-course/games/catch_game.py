import pygame
import random
import os

from games.game import Game
from enums.action import Action


class CatchGame(Game):
    
    def __init__(self):
        super().__init__(
            os.getenv('CATCH_NAME', 'Catch Game'),
            int(os.getenv('CATCH_GRID_WIDTH', 400)),
            int(os.getenv('CATCH_GRID_HEIGHT', 400))
        )
        self.BALL_VELOCITY = int(os.getenv('CATCH_BALL_VELOCITY', 20))
        self.BALL_WIDTH = 20
        self.BALL_HEIGHT = 20
        self.PADDLE_WIDTH = 50
        self.PADDLE_HEIGHT = 10
        self.PADDLE_VELOCITY = 20
        self.GAME_FLOOR = 350
        self.GAME_CEILING = 10

    def reset(self):
        super().reset()
        self.paddle_x = self.GAME_WIDTH // 2
        self.ball_x = random.randint(0, self.GAME_WIDTH-20)
        self.ball_y = self.GAME_CEILING

    def execute_action(self, action):
        if action == Action.LEFT.value:
            self.paddle_x -= self.PADDLE_VELOCITY
            if self.paddle_x < 0:
                self.paddle_x = self.PADDLE_VELOCITY
        elif action == Action.RIGHT.value:
            self.paddle_x += self.PADDLE_VELOCITY
            if self.paddle_x > self.GAME_WIDTH - self.PADDLE_WIDTH:
                self.paddle_x = self.GAME_WIDTH - self.PADDLE_WIDTH - self.PADDLE_VELOCITY
        else:
            action = Action.NOTHING.value
            pass
        self.environment_action = action

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
