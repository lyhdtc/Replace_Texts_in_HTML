import sys
import os


def readname(picpath):
    name = os.listdir(picpath)
    return name

def rplace(newname,path, new_file_name):
    old = "00_neutral.jpg"

    with open(path, "r+", encoding="utf-8") as filetext:
        lines = filetext.read()
        filetext.seek(0)
        lines = lines.replace(old, newname)
        print(new_file_name)
        fp = open(new_file_name, "w+", encoding="utf-8")
        fp.write(lines)
        fp.close()



if __name__ == "__main__":
    #path = "old/2109Emotion01.html"
    #picpath = "img\emo05\Emotion"

    #旧的html的路径
    path = "old/2109Exp1.html"
    #要替换的新图片的路径
    picpath = "img\emo05\Exp"

    name = readname(picpath)
    count = 0
    for i in name:
        #这里要修改好，对应旧文件的新文件的名字，是前缀+编号格式的
        new_file_name = "2109Exp" + str(count) + ".html"
        #第一个参数是替换的文本内容，如果要修改文件位置的话需要像下面一样增加字符串路径
        rplace("Exp/"+i, path, new_file_name)
        count = count+1

