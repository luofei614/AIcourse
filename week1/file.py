import json
import os
with open('./a.json','w',encoding="utf-8") as f:
    f.write(json.dumps({"a":"中文a","b":"中文b"},ensure_ascii=False)+"\n")
    f.write(json.dumps({"c":"中文c","d":"中文d"},ensure_ascii=False)+"\n")

with open('./a.json','r') as f:
    for line in f.readlines():
        print(json.loads(line))

print(os.listdir('./'))
print(list(os.walk('./'))) 
for parent,dirnames,filenames in os.walk('./'):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for dirname in  dirnames:                       #输出文件夹信息
        print(os.path.join(parent, dirname))  # 输出文件夹路径信息
    for filename in filenames:  # 输出文件信息
        print(os.path.join(parent, filename))  # 输出文件路径信息
os.mkdir('./aaa')