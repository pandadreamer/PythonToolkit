'''
将String按照分隔符划分成一个个词并保存在list中

Jack|0|fine~  --> ['Jack', '0', 'fine']

split(str=' ', num= split_count)

'''

import codecs
import sys

f = codecs.open('train.txt', 'r', encoding="utf-8")
lines = f.readlines()

lists = []

for i in range(len(lines)):
    lists.append(lines[i].split('|',2))