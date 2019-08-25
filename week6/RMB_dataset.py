#识别人民币的程序
import tensorflow as tf
import pathlib
import os
import numpy as np
data_root = pathlib.Path('./img')
labelset=[]
labelsdict={}
labels=[]
datas=[]
with open('./label.txt','r') as f:
    for line in f.readlines():
        s=line.split(" ")
        key=s[0].strip()
        value=s[1].strip()
        if value not in labelset:
            labelset.append(value)
        labelsdict[key]=labelset.index(value)

for path in data_root.iterdir():
    key=os.path.splitext(os.path.basename(path))[0]
    labels.append(labelsdict[key])
    datas.append(str(path))


def load_image(path):
    image=tf.io.read_file(path)
    imagedata=tf.image.decode_jpeg(image,channels=3)
    imagedata=tf.image.resize(imagedata,[100,100])
    imagedata /= 255
    return imagedata

def random_image(image):
    image=tf.image.random_flip_left_right(image)
    image=tf.image.random_flip_up_down(image)
    image=tf.image.random_hue(image,0.08) #色相
    image=tf.image.random_saturation(image,0.6,1.6) #饱和度
    image=tf.image.random_brightness(image,0.05) #亮度
    image=tf.image.random_contrast(image,0.7,1.3) #对比度
    return image

data=tf.data.Dataset.from_tensor_slices((datas,labels))
data=data.map(map_func=lambda x,y: (load_image(x),y))
data=data.concatenate(data.map(map_func=lambda x,y: (random_image(x),y)))
data=data.repeat(10).batch(10)
'''
train_data=[load_image(d) for d in datas]
train_data+=[random_image(d) for d in train_data]
train_data=np.array(train_data) #这里运行很慢， 需要换成dataset的形式。
labels+=labels
'''


model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(100,100,3)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(len(labelset),activation="softmax")
])


model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['acc']
             )


model.fit(data,epochs=5)

imagedata=load_image('./img/2.jpeg')
y=model.predict(np.array([imagedata]))
print(y)
print('预测结果:%s' % labelset[np.argmax(y,axis=1)[0]])