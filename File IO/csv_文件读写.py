import pandas as pd
import numpy as np

'''
csv读取文件操作
'''

data = pd.read_csv("xxx.csv")

# 假设xxx.csv中有两列，分别叫做 price 和 label
# 转换成numpy类型
price = np.array(data['price'])
label = np.array(data['label'])


'''
csv写文件操作
'''

price = np.zeros([100])
label = np.ones([100])

# Way 1:
price_col = pd.Series(price, name="Price")
label_col = pd.Series(label, name="Label")

fin = pd.concat([price_col, label_col], axis=1)
fin.to_csv('xxx.csv', index=False)


# Way 2:
fin = pd.DataFrame({'Price':price, 'Label':label})
fin.to_csv('xxx.csv', index=False)