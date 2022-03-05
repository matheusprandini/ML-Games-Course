import os
import numpy as np

from random import shuffle
from tensorflow.keras import *


class NnModel(object):

    def __init__(self):
        self.model_name = os.getenv('MODEL_NAME')
        self.color = os.getenv('COLOR_MODE')

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

    def convert_input_shape(self, inputs):
        input_shape = inputs[0].shape
        converted_input_shape = input_shape + (1,) if self.color == 'GRAYSCALE' else input_shape
        converted_input_shape = (-1,) + (np.prod(converted_input_shape),) if self.model_mode == 'MLP' else (-1,) + converted_input_shape
        return converted_input_shape

    def training(self, data, batch_size, epochs, optimizer_name, split_fraction):
        inputs, labels = self.generate_input_and_output_data(data)

        inputs_train, labels_train, inputs_test, labels_test = self.splitting_data(inputs, labels, split_fraction)
        
        input_shape = self.convert_input_shape(inputs_train)
        num_classes = len(set(labels_train))

        inputs_train = np.array(inputs_train).reshape(input_shape)
        labels_train = utils.to_categorical(labels_train, num_classes)
        inputs_test = np.array(inputs_test).reshape(input_shape)
        labels_test = utils.to_categorical(labels_test, num_classes)

        self.compile(optimizer_name)

        self.model.fit(inputs_train, labels_train, batch_size=batch_size,
                    validation_data=(inputs_test, labels_test), epochs=epochs)

        self.save_model()

    def predict(self, input):
        return np.argmax(self.model.predict(input))

    def save_model(self):
        self.model.save(self.model_name)
