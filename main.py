import os

from Games.CatchGame import CatchGame
from Games.SnakeGame import SnakeGame
from Players.RandomPlayer import RandomPlayer


games_translator = {
    'Catch': CatchGame(),
    'Snake': SnakeGame()
}

players_translator = {
    'Random': RandomPlayer()
}

if __name__ == '__main__':
    game = games_translator[os.getenv('GAME', 'Catch')]
    player = players_translator[os.getenv('PLAYER', 'Random')]
    num_tries = int(os.getenv('NUM_TRIES', 10))

    for i in range(num_tries):
        print(f"Try: {i}")
        game.reset()
        frame = game.get_frame()
        game_over = False
        while not game_over:
            action = player.choose_action(frame)
            frame, reward, game_over, score = game.step(action)
            print(f"Action: {action}",
                f"Reward: {reward}",
                f"Game Over: {game_over}",
                f"Score: {score}")
