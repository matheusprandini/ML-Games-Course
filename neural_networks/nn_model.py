import os
import numpy as np

from random import shuffle
from tensorflow.keras import *


class NnModel(object):

    def __init__(self):
        self.model_name = os.getenv('MODEL_NAME')

    def generate_input_and_output_data(self, data):
        input_data = []
        output_data = []
        shuffle(data)

        for example in data:
            img = example[0]
            output = example[1]
            input_data.append(img)
            output_data.append(output)

        return input_data, output_data


    def splitting_data(self, inputs, labels, split_fraction=0.8):

        number_examples = len(inputs)

        split = int(split_fraction * number_examples)

        x_train = inputs[:split]
        x_test = inputs[split:]
        y_train = labels[:split]
        y_test = labels[split:]
        
        return x_train, y_train, x_test, y_test

    def training(self, data, batch_size=64, epochs=100, split_fraction=0.8):
        inputs, labels = self.generate_input_and_output_data(data)

        inputs_train, labels_train, inputs_test, labels_test = self.splitting_data(inputs, labels, split_fraction)
        input_shape = (-1, 32*32)
        inputs_train = np.array(inputs_train).reshape(input_shape) 
        labels_train = utils.to_categorical(labels_train, num_classes=3)
        inputs_test = np.array(inputs_test).reshape(input_shape)
        labels_test = utils.to_categorical(labels_test, num_classes=3)

        self.compile()

        self.model.fit(inputs_train, labels_train, batch_size=batch_size,
                    validation_data=(inputs_test, labels_test), epochs=epochs)

        self.save_model()

    def predict(self, input):
        return np.argmax(self.model.predict(input))

    def save_model(self):
        self.model.save(self.model_name)
