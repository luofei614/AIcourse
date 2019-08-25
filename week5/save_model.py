import tensorflow as tf
import random
import numpy as np
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) =mnist.load_data()

x_train,x_test=x_train/255,x_test/255
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10,activation="softmax")
])
#保存网络为yaml 或 json

yaml=model.to_yaml()
json=model.to_json()
print(yaml)
model=tf.keras.models.model_from_yaml(yaml)

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])



model.fit(x_train,y_train,batch_size=10,epochs=5,validation_split=0.2)


#保存权重
model.save_weights('./weights')
model.load_weights('./weights')

#保存整个模型
model.save('./all_model.h5')
