'''
将图像转换成.py文件，方便将图像也打包进exe文件

其他文件调用图像代码文件时:
    from memory_pic import *
    import base64
    from PIL import Image
    import os

    def get_pic(pic_code, pic_name):
        image = open(pic_name, 'wb')
        image.write(base64.b64decode(pic_code))
        image.close()

    get_pic(input_png, 'input.png')
    get_pic(mask_png, 'mask.png')

    input=Image.open('./input.png')
    mask=Image.open('./mask.png')

    os.remove('input.png')
    os.remove('mask.png')
'''

import base64
 
def pic2py(picture_names, py_name):
    write_data = []
    for picture_name in picture_names:
	    filename = picture_name.replace('.', '_')
	    open_pic = open("%s" % picture_name, 'rb')
	    b64str = base64.b64encode(open_pic.read())
	    open_pic.close()
	    write_data.append('%s = "%s"\n' % (filename, b64str.decode()))

    f = open('%s.py' % py_name, 'w+')
    for data in write_data:
    	f.write(data)
    f.close()
 
if __name__ == '__main__':
    pics = ["input.png", "mask.png"]
    pic2py(pics, 'memory_pic')
    print("ok")
