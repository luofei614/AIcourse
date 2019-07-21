import tensorflow as tf
#数组式
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10,activation="softmax")
])
#添加式
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128,activation="relu"))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(10,activation="softmax"))
#函数式
'''
inputs=tf.keras.Input(shape=(28,28))
h1=tf.keras.layers.Flatten(input_shape=(28,28))(inputs)
h2=tf.keras.layers.Dense(128,activation="relu")(h1)
h3=tf.keras.layers.Dropout(0.2)(h2)
outputs=tf.keras.layers.Dense(10,activation="softmax")(h3)
model=tf.keras.Model(inputs=inputs,outputs=outputs)
'''
model.summary()