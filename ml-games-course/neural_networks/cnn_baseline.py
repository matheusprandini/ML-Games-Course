from tensorflow.keras import *

from neural_networks.nn_model import NnModel


class CnnBaseline(NnModel):

    model_mode = 'CNN'

    def build(self, input_shape, output_neurons):
        #
        # Your code here
        #
        self.model.summary()
