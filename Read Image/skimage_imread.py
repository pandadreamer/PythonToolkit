from skimage import io
import numpy as np

# 该方法获取到的是 numpy 类型的数组
x = io.imread("xxx.png")

# x.shape: (height, width, channel)
# 使用不同框架可能需要对其进行
# 如 torch.nn 中的要求维度是 (Batch_size, Channel, Height, Weight)
# 因此对图片需要做如下变换：(height, width, channel) --> (channel, height, width)
x = x.transpose((2,0,1))
# x.shape: (channel, height, width)

# or 
'''
x = x[:,:,:,None]
x = x.transpose((3, 2, 0, 1))
'''