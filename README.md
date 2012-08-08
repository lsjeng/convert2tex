convert2tex
===========

Convert pdb/epub/txt to tex file and from Simple Chinese to Traditional Chinese

## 功能

### convert2tex.py

* 可將 epub/txt/pdb (限好讀網站格式)，轉換成純文字的 xelatex 檔。
* 預設轉換出來的 tex 支援直書。
* 支援簡體轉繁體(支援字詞轉換)。

### epubs2t.py

* 支援 epub 檔簡體轉繁體(支援字詞轉換)。

## 安裝

1. 安裝 [python-jianfan](http://code.google.com/p/python-jianfan/) 套件

        pip install jianfan

2. 將 `*.py` 檔下載下來後複製到可執行路徑下，即可使用。

        git clone https://github.com/yen3/convert2tex.git
        cd convert2tex
        cp *.py /usr/local/bin

## 使用

直接在 command line 使用即可，如果想要看更詳盡的資訊請分別輸入。

	./convert2tex.py -h

及

	./epubs2t.py

## 感謝

* 簡繁互換的字典檔是使用新同文堂[技術資料](http://tongwen.openfoundry.org/technical_zh-tw.htm): [word_s2t.txt](http://tongwen.openfoundry.org/src/tongwen_table/word_s2t.txt) 和 [phrase_s2t.txt](http://tongwen.openfoundry.org/src/tongwen_table/phrase_s2t.txt)，在此感謝

* 程式的簡繁互換參考 [鳥毅的Blog: 完美簡繁轉換](http://blog.tenyi.com/2011/08/blog-post.html) 進行修改，在此感謝。
