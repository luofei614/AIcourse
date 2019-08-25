import  tensorflow as tf
import  numpy as np
model=tf.keras.models.load_model('./all_model.h5')
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) =mnist.load_data()
y=model.predict(np.array([x_test[0]]))
print('预测结果:%s' % np.argmax(y,axis=1)[0])
print('真实结果: %s' % y_test[0])