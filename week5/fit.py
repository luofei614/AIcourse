import tensorflow as tf
import numpy as np
#显示图片
import matplotlib.pyplot as plt
def plot_image(image):
    fig=plt.gcf()
    fig.set_size_inches(2,2)
    plt.imshow(image,cmap='binary')
    plt.show()

def show_train_history(train_history,train,validation):
    print(train_history.history)
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train','validation'],loc='upper left')
    plt.show()

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) =mnist.load_data()
#显示一张图片
plot_image(x_train[0])
print("图片的值：%s" % y_train[0])

x_train,x_test=x_train/255,x_test/255
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10,activation="softmax")
])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),loss=tf.keras.losses.SparseCategoricalCrossentropy(),metrics=[tf.keras.metrics.SparseCategoricalAccuracy()])
#train_history=model.fit(x_train,y_train)
train_history=model.fit(x_train,y_train,batch_size=10,epochs=5,validation_split=0.2)
show_train_history(train_history,'sparse_categorical_accuracy','val_sparse_categorical_accuracy')

#评估模型
evalute_ret=model.evaluate(x_test,y_test)
print('评估结果：')
print(evalute_ret)
#预测
y=model.predict(np.array([x_test[0]]))
print('预测结果')
print(np.argmax(y,axis=1))
print('真实结果')
print(y_test[0])


