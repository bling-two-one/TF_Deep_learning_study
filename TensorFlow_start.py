import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np

#데이터 준비
#1.임의의 무작위 데이터 셋 사용(numpy 사용)
x = np.random.sample((100, 3))
dateset = tf.data.Dataset.from_tensor_slices(x)

#2.텐서플로에서 제공하는 데이터셋 사용
ds = tfds.load('mnist', split='train', shuffle_files=True)
