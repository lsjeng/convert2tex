#-*- coding: utf8 -*-

from jianfan import jtof

# http://chardet.feedparser.org
from dic_tw import dic_tw

# 最大正向匹配
def convertVocabulary(string_in, dic):
    i=0
    s = string_in
    while i < len(s):
        for j in range(len(s) - i +1, 0, -1):
            if s[i:j] in dic:
                t = dic[s[i:j]]
                s = s.replace(s[i:j], t) 
                i += len(t) -1
                break
        i += 1

    return s 

def convert_UTF8_content(content):
    newcontent = jtof(content)
    return "\n".join([convertVocabulary(line, dic_tw()) for line in newcontent.splitlines()])
        
			
