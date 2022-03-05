import os

from tensorflow.keras.optimizers import Adam, RMSprop, SGD


class Optimizer():

    translator = {
        'adam': Adam,
        'rmsprop': RMSprop,
        'sgd': SGD
    }

    @classmethod
    def get(cls, name):
        if name not in cls.translator:
            name = 'adam'
        optimizer = cls.configure(cls.translator[name])
        return optimizer

    @classmethod
    def configure(cls, base_optimizer):
        return base_optimizer(
            learning_rate=float(os.getenv('LEARNING_RATE', 0.05))
        )
