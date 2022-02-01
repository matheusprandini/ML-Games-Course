from tensorflow.keras import *

from neural_networks.nn_model import NnModel


class MlpBaseline(NnModel):

    def build(self, input_shape, output_neurons):
        model = Sequential()
        model.add(layers.Dense(1024, activation='relu', input_shape=input_shape))
        model.add(layers.Dense(1024, activation='relu'))
        model.add(layers.Dense(output_neurons, activation='sigmoid'))

        model.summary()
		
        return model

    def compile(self):
        self.model.compile(optimizer=optimizers.SGD(lr=0.05, momentum=0.0, decay=0.0, nesterov=False), loss='mean_squared_error', metrics=['accuracy'])
