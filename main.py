# encoding: utf-8
import os
import re
import glob
import nltk
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download()
np.set_printoptions(precision=4) # 表示のフォーマットを指定 (有効数字4桁)


fileroots = [
    './reviews/Mercari/',
    ]
files = os.listdir(fileroots[0]) # ./BBB/ 以下のファイルを全部取得

docs = [] # 分析に用いる文書ファイル集合

garbages = [
    "the",
    "it",
    "and",
    "of",
    "on",
    "is",
    "with",
    "to",
    "for",
    "in",
    "that",
    "from",
    "so",
    "my",
    "was",
    "by",
    "at"
]

for (i, file) in enumerate(files):
    if i == 0: continue # 1つ目のファイルは ".DS_Store"のため無視
    doc = open(fileroots[0] + file).read().lower() # 小文字化して文書を取得

    doc = doc.replace("\n", " ") # 改行文字の削除
    doc = re.sub(re.compile("[!-/:-@[-`{-~]"), " ", doc) # 半角記号の削除
    doc = re.sub(r'[0-9]+', "", doc) # 半角数字の削除

    for garbage in garbages:
        doc = doc.replace(garbage, "") # 改行文字の削除


    docs.append(doc)


vectorizer = TfidfVectorizer(use_idf=True)
vecs = vectorizer.fit_transform(docs)
words = sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1])

dic_list = []
for vec in vecs.toarray():
    dic = {}
    for i in range(len(vec)):
        dic[words[i][0]] = vec[i]
        #dic.append({words[i][0]: vec[i]})
    for k, v in sorted(dic.items(), key=lambda x:-x[1]):
        if v == 0.0: break;
        print str(k) + ", " + str(v)
    print "---------------"

#print vectorizer.vocabulary_.items()['saying'][1]


#for k,v in sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1]):
#    print k,v
