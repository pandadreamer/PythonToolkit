import codecs
import sys

'''
'r', read only
'w', write only
'a', change to file ending
'r+', write and read 
'''

# 查看内容
f = codecs.open('xxx.txt', 'r', encoding="utf-8")
lines = f.readlines()

for i in range(len(lines)):
    print(lines[i])

# 重写内容

f = codecs.open('xxx.txt', 'w', encoding="utf-8")

f.write("Hello world\r\n")

# 在文件未写

f = codecs.open('xxx.txt', 'a', encoding="utf-8")
f.write("Hello world\r\n")