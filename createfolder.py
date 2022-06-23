# -*- coding: utf-8 -*-
import os


def main(path):
    if path == '':
        path = os.path.abspath('.')
    # regr = re.compile(r'\w*\|\w*')
    f = open("englist_list.txt", "r", encoding='utf_8')
    fl = f.readlines()  # readlines reads the individual lines into a list
    for x in fl:
        y = x.replace('|', '').replace('\n', '').replace(':', '').replace('?', '')
        y1 = os.path.join(path, y)
        if not os.path.isdir(y1):
            os.mkdir(y1)
            z = os.path.abspath(y1)
            print("folder %s created" % z)
            os.mkdir(os.path.join(z, "文本精讲"))
            print("folder %s created" % (os.path.join(z, "文本精讲")))
            os.mkdir(os.path.join(z, "亮解单词"))
            print("folder %s created" % (os.path.join(z, "亮解单词")))
            os.mkdir(os.path.join(z, "带读训练"))
            print("folder %s created" % (os.path.join(z, "带读训练")))
            os.mkdir(os.path.join(z, "听说练习"))
            print("folder %s created" % (os.path.join(z, "听说练习")))


if __name__ == '__main__':
    main(r'C:\ShaneLib\EnglishLearn\Recitation Camp')
