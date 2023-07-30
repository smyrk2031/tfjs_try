import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist

# データセットの準備
print("データセットの準備")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train[:, :, :, np.newaxis].astype("float32") / 255.0  # (60000, 28, 28, 1)
x_test = x_test[:, :, :, np.newaxis].astype("float32") / 255.0    # (10000, 28, 28, 1)


# モデルの準備
print("モデルの準備")
model = Sequential([
  Conv2D(32, kernel_size=(3, 3), activation="relu", padding="same", input_shape=(28, 28, 1)),
  MaxPooling2D(pool_size=(2, 2)),
  Conv2D(64, kernel_size=(3, 3), activation="relu", padding="same"),
  MaxPooling2D(pool_size=(2, 2)),
  Flatten(),
  Dense(128, activation="relu"),
  Dense(10, activation="softmax")
])
model.compile("Adam", loss="sparse_categorical_crossentropy", metrics="sparse_categorical_accuracy")
# 学習
print("学習")
model.fit(x_train, y_train, batch_size=256, epochs=10, validation_data=(x_test, y_test))


import tensorflowjs as tfjs
print("TFJSコンバート出力")
tfjs.converters.save_keras_model(model, "./tfjs_model")
