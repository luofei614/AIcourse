import tensorflow as tf
import numpy as np
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10,activation="softmax")
])
#model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
x=np.random.rand(10000,28,28)
y=np.random.rand(10000)
print(y)
model.fit(x,y)