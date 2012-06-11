#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys
import zipfile
import s2c 

def main():
    epub_fn_list = []
    if len(sys.argv) != 2:
        print "epubs2c.py sample.epub"
    else:
        epub_fn_list = sys.argv[1:]

    for fh in epub_fn_list:
        fh = zipfile.ZipFile(sys.argv[1], "r")
        fn_list = [fn for fn in fh.namelist() if fn.endswith('html') or fn.endswith('htm')]
        fn_list_2 = [fn for fn in fh.namelist() if not fn.endswith('html') and not fn.endswith('htm')] 

        content_list = [s2c.convert_UTF8_content(fh.read(fn)).replace('zh-CN', 'zh-TW') for fn in fn_list]
        content_list_2 = [fh.read(fn) for fn in fn_list_2]

        fh.close()

        fh = zipfile.ZipFile(sys.argv[1], "w")
        for fn, content in zip(fn_list, content_list):
            fh.writestr(fn, content.encode('UTF-8'))

        for fn, content in zip(fn_list_2, content_list_2):
            fh.writestr(fn, content)

        fh.close()

if __name__ == "__main__":
    main()
