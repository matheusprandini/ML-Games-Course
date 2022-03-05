import os


class Loss():

    @classmethod
    def get(cls):
        return os.getenv('LOSS_NAME', 'mean_squared_error')
