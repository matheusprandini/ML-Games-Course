from tensorflow.keras.models import *
from keras.layers.core import Activation, Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam
from keras.regularizers import l2
from neural_networks.nn_model import NnModel


class CnnBaseline(NnModel):

    def build(self, input_shape, output_neurons):
        model = Sequential()

        model.add(Conv2D(20, kernel_size=(7,9), padding="same",
                        input_shape=input_shape,
                        kernel_regularizer=l2(0.)))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
            
        model.add(Conv2D(50, kernel_size=(5,5), padding="same",
                        kernel_regularizer=l2(0.)))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
            
        model.add(Conv2D(70, kernel_size=(4,5), padding="same",
                        kernel_regularizer=l2(0.)))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
            
        model.add(Flatten())

        model.add(Dense(500))
        model.add(BatchNormalization())
        model.add(Activation("relu"))
        model.add(Dropout(0.5))
            
        model.add(Dense(output_neurons))
        model.add(BatchNormalization())
        model.add(Activation("softmax"))
        
        model.summary()

        return model
    
    def compile(self):
        self.model.compile(optimizer=Adam(),
                loss='categorical_crossentropy',
                metrics=['accuracy'])
