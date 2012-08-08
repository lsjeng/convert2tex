#-*- coding: utf8 -*-

from jianfan import jtof
# http://chardet.feedparser.org
#from dic_tw import dic_tw

WORD_DICTIONARY_PATH = "word_s2t.txt"
PHASE_DICTIONARY_PATH = "phrase_s2t.txt"

class DictionarySingleton(object):
    _instance = None
    def __init__(self):
        f = open(WORD_DICTIONARY_PATH, 'r')
        self.w_dict = dict([tuple(l.split(',')[0:2]) for l in f.read().split('\r\n')])
        f.close()

        f = open(PHASE_DICTIONARY_PATH, 'r')
        self.p_dict = dict([tuple(l.split(',')[0:2]) for l in f.read().split('\r\n')])
        f.close()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DictionarySingleton, cls).__new__(
                                cls, *args, **kwargs)


        return cls._instance

    def word_dic(self):
        return self.w_dict

    def phase_dic(self):
        return self.p_dict


# only one instance 
TRANSLATE_DICTIONARY = DictionarySingleton()

def convert_word(s_string, w_dic):
    t_string = s_string
    for i in xrange(0, len(t_string)-1):
        if t_string[i] in w_dic:
            t_string = t_string.replace(t_string[i:i+1], w_dic[t_string[i]])
    
    return t_string

def convert_phase(string_in, dic):
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
    content_lines = [convert_word(l, TRANSLATE_DICTIONARY.word_dic()) for l in newcontent.splitlines()]
    
    return "\n".join([convert_phase(l, TRANSLATE_DICTIONARY.phase_dic()) for l in content_lines])

