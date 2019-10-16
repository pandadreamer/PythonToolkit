import json

'''
json读取操作
'''

with open("xxx.json" ,'r') as f:
    data = json.load(f)

# 假设data.keys()返回的是 'images', 'dataset'
# 假设data['images']是一个list
# 假设data['images'][0].keys()返回的是 'imgid', 'filename'

imgid=[]
filename=[]
for img in data['images']:
    imgid.append(img['imgid'])
    filename.append(img['filename'])

'''
json写操作
'''

data = {'images':[{'imgid':0, 'filename':"coco0"}, {'imgid':1, 'filename':"coco1"}], 'dataset':"coco"}

with open("xxxx.json" ,'w') as f:
    json.dump(data, f)