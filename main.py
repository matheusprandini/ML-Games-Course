import os

from Games.CatchGame import CatchGame
from Games.SnakeGame import SnakeGame
from Agents.RandomAgent import RandomAgent


games_translator = {
    'Catch': CatchGame(),
    'Snake': SnakeGame()
}

agents_translator = {
    'Random': RandomAgent()
}

if __name__ == '__main__':
    game = games_translator[os.getenv('GAME', 'Catch')]
    agent = agents_translator[os.getenv('AGENT', 'Random')]
    num_tries = int(os.getenv('NUM_TRIES', 10))

    for i in range(num_tries):
        print(f"Try: {i}")
        game.reset()
        frame = game.get_frame()
        game_over = False
        while not game_over:
            action = agent.choose_action(frame)
            frame, reward, game_over, score = game.step(action)
            print(f"Action: {action}",
                f"Reward: {reward}",
                f"Game Over: {game_over}",
                f"Score: {score}")
