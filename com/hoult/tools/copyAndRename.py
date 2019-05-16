# -*- coding:utf8 -*-
## win10壁纸迁移脚本 将windows聚焦锁屏壁纸复制到给定文件下
# shutil 复制工具包， Image 图片处理包
import os
import shutil
from PIL import Image

class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = 'C:\\Users\\利超\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets'
        self.dst = 'D:\\Hu_life\\Pictures\\desktop_wallpaper\\win10聚焦'
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            # if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(self.path), item)
            img = Image.open(src)
            print(img.size)
            dst = os.path.join(os.path.abspath(self.dst), str(i) + '.jpg')
            try:
                if img.size == (1920, 1080):
                    shutil.copy(src, dst)
                    # os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
            except:
                continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))
if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()