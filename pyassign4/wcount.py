#!/usr/bin/env python3 

"""wcount.py: count words from an Internet file. 

_author_ = "Wangyiyong"
_pkuid_ = "1800011763"
_email_ = "1800011763@pku.edu.cn"
""" 
import string 
import sys 
from urllib.request import urlopen 

def wcount(lines,topn): 
    strin = lines.decode() # 转化为字符串 
    for c in string.punctuation: 
        if c != "'": 
            strin = strin.replace(c," ") # 除单引号外，把所有的标点替换为空格 
    strin = strin.lower() 
    l1 = strin.split()
    l2 = list(set([(i,l1.count(i)) for i in l1])) 
    l2.sort(key=lambda x: x[1], reverse=True) 
    lens = len(l2) 
    if topn > lens: 
        for i in l2: 
            print(i[0], " ", i[1])  
    else: 
        for i in l2[:n]:
            print(i[0], " ", i[1]) 

if __name__ == '__main__': 
""" sys.argv 通过命令提示行得到的列表，一定存在第一项，为文件名。 """ 
    if len(sys.argv) == 1: 
# 命令行仅给了一个参数，则无法找到网页，无法计数 
        print('Usage: {} url [topn]'.format(sys.argv[0])) 
        print(' url: URL of the txt file to analyze ') 
        print(' topn: how many (words count) to output. If not given, will output top 10 words') 
        sys.exit(1) 
    text = urlopen(sys.argv[1]) 
    text0 = text.read() 
    text.close() 
    if len(sys.argv) == 2: 
# 命令行给了2个参数，给出仅给出十个结果 
        wcount(text0, 10) 
    if len(sys.argv) == 3: 
# 命令行给了3个参数，  
        wcount(text0, int(sys.argv[2])) 
    if len(sys.argv) > 3: 
        print("输入的参数多于应该输入的参数") 
