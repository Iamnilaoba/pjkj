import os

basedir = os.path.dirname(os.path.dirname(__file__))
path = os.path.join(basedir,"imgs")
if not os.path.exists(path):
    os.mkdir(path)

# 路径
ps = os.path.join(path,'中控')
if not  os.path.exists(ps):
    os.mkdir(ps)

# 文件
fileps = os.path.join(ps,"1.png")
with open(fileps,'wb') as f:
    f.write(b"aaa")
