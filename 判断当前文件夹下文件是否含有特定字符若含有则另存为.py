import glob
import os
import shutil
from 读取txt文件内容到列表 import get_content

def existence_or_no(key_list):
    # keyword = "1"
    flag = 0
    base_path = os.getcwd()
    target_path = os.path.join(base_path,"all")
    if os.path.exists(target_path):
        a = 1 # 随便写个让程序得以运行
    else:
        os.makedirs(target_path)

    filenames = glob.glob(base_path+"\*.htm")
    for i in filenames:
        with open(i,"r",encoding="UTF-8")as fo:
            file = fo.read()
            # if file.count(keyword) == 0:
            for j in key_list:
                if file.count(j) != 0:
                    flag = 1
                    try:
                        fo.close()
                        shutil.move(i, target_path)
                        print(f"{i}存在关键词并移动成功")
                    except:
                        print(f"{i}存在关键词并但移动失败")
                    break
            if flag == 0:
                print(f"{i}不存在关键词")
            flag = 0
key_list = get_content("词库.txt")
existence_or_no(key_list)