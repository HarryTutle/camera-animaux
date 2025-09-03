# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 17:50:07 2025

@author: thoma
"""

import tensorflow as tf
from tensorflow.keras.applications import ResNet50, MobileNet
from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D, Dropout, Conv2D, Input, Lambda, MaxPooling2D, Concatenate, BatchNormalization, Add, Activation
from tensorflow.keras.models import Model, Sequential, load_model
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.regularizers import L2, L1
import pandas as pd
import matplotlib.pyplot as plt

batch=10

train_datagen = ImageDataGenerator(
    rescale=1./255,
    zoom_range=(0.4, 1),
    width_shift_range=0.4,
    height_shift_range=0.3,
    shear_range=0.1,
    rotation_range=0.4,
    horizontal_flip=True,
    brightness_range=[0.8, 1.2],
    fill_mode='nearest'
    
)

test_datagen = ImageDataGenerator(
    rescale=1./255
    
    
    )

valid_datagen = ImageDataGenerator(
    rescale=1./255
    )

train_generator = train_datagen.flow_from_directory(
    'C:/Users/thoma/Documents/robot sentinelle/2 mars 2025/google datasets/train',
    target_size=(224, 224),
    batch_size=batch,
    class_mode='categorical',  # Ou "binary" pour 2 classes
    color_mode='rgb',
    shuffle=True
)

test_generator = test_datagen.flow_from_directory(
    'C:/Users/thoma/Documents/robot sentinelle/2 mars 2025/google datasets/test',
    target_size=(224, 224),
    batch_size=batch,
    class_mode='categorical',
    color_mode='rgb',
    shuffle=False
)

valid_generator = valid_datagen.flow_from_directory(
    'C:/Users/thoma/Documents/robot sentinelle/2 mars 2025/google datasets/valid',
    target_size=(224, 224),
    batch_size=batch,
    class_mode='categorical',
    color_mode='rgb',
    shuffle=False
    )


print(train_generator.class_indices)
print(test_generator.class_indices)
print(valid_generator.class_indices)

model_base=MobileNet(weights='imagenet', include_top=False)
print(model_base.summary())

avg=GlobalAveragePooling2D()(model_base.output)
output=Dense(5, activation='softmax')(avg)
model=Model(inputs=model_base.input, outputs=output)

for layer in model_base.layers:
    layer.trainable=False
    
optimizer=Adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history=model.fit(train_generator, epochs=12, validation_data=test_generator)

for layer in model_base.layers:
    layer.trainable=True
    
optimizer=Adam(lr=0.0001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
history=model.fit(train_generator, epochs=10, validation_data=test_generator)


model.save("mobilenet_220625_2.h5")