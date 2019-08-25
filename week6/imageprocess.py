import tensorflow as tf
import matplotlib.pyplot as plt
import  numpy as np
imagevalue=tf.io.read_file('./img/1.jpeg')
imagedata=tf.image.decode_jpeg(imagevalue)

plt.imshow(imagedata)
plt.show()
resized=tf.image.resize(imagedata,[300,300])
resized=np.asarray(resized, dtype='uint8') #要unit8格式才能正常显示，这里需要转换一下
plt.imshow(resized)
plt.show()
#裁剪或填充
resized=tf.image.resize_with_crop_or_pad(imagedata,300,300)
plt.imshow(resized)
plt.show()
#翻转：（上下，左右，对角线）
flipped=tf.image.flip_up_down(imagedata)
plt.imshow(flipped)
plt.show()

flipped=tf.image.flip_left_right(imagedata)
plt.imshow(flipped)
plt.show()

flipped=tf.image.transpose(imagedata)
plt.imshow(flipped)
plt.show()

#随机翻转
flipped=tf.image.random_flip_up_down(imagedata)
plt.imshow(flipped)
plt.show()

#亮度

adjusted=tf.image.adjust_brightness(imagedata,0.5)
print(adjusted)
#adjusted=np.asanyarray(adjusted, dtype='uint8')
#d=tf.clip_by_value([1,2,3,4,5,6,7,8,19],0,1)
#print(d)
plt.imshow(adjusted)
plt.show()

#随机亮度
adjusted=tf.image.random_brightness(imagedata,0.5)
plt.imshow(adjusted)
plt.show()

#对比度
adjusted=tf.image.adjust_contrast(imagedata,0.5)
plt.imshow(adjusted)
plt.show()
adjusted=tf.image.adjust_contrast(imagedata,5)
plt.imshow(adjusted)
plt.show()
#随机对比度
adjusted=tf.image.random_contrast(imagedata,0.5,5)
plt.imshow(adjusted)
plt.show()

#色相
adjusted=tf.image.adjust_hue(imagedata,0.9)
plt.imshow(adjusted)
plt.show()
#随机色相
adjusted=tf.image.random_hue(imagedata,0.5)
plt.imshow(adjusted)
plt.show()

#饱和度
adjusted=tf.image.adjust_saturation(imagedata,5)
plt.imshow(adjusted)
plt.show()
#随机饱和度
adjusted=tf.image.random_saturation(imagedata,1,5)
plt.imshow(adjusted)
plt.show()
#标注框
#result=tf.image.draw_bounding_boxes(imagedata,[[10,10,100,100],[20,20,40,40]],[(0, 0, 0),(0, 0, 0)])
