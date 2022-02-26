from tensorflow.keras import *

from neural_networks.nn_model import NnModel


class MlpBaseline(NnModel):

    model_mode = 'MLP'

    def build(self, input_shape, output_neurons):
        self.model = Sequential()
        self.model.add(layers.Dense(1024, activation='relu', input_shape=input_shape))
        self.model.add(layers.Dense(1024, activation='relu'))
        self.model.add(layers.Dense(output_neurons, activation='sigmoid'))

        self.model.summary()

    def compile(self, learning_rate):
        self.model.compile(optimizer=optimizers.SGD(lr=learning_rate, momentum=0.0, decay=0.0, nesterov=False), loss='mean_squared_error', metrics=['accuracy'])
