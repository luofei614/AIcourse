from gensim import  corpora,similarities,models
import  numpy as np
import jieba
import os
import pickle
input_str=input("请输入一个问题：") or "越南旅游需要带插头转换器吗";
if os.path.isfile('./simlarity.bin'):
    simlarity=similarities.Similarity.load('./simlarity.bin')
    dictionary=corpora.Dictionary.load("./dict.bin")
    text=pickle.load(open("./text.bin","rb"))
    tfidf=models.TfidfModel.load("./tfidf.bin")
else:
    sentences=[]
    text=[]
    stop_words=["，",'。','？','.',',','.','的',' ','\n']
    with open('./questions.txt',encoding="utf-8") as f:
        for  line in f.readlines():
            sentences.append([word for word in jieba.cut(line) if word not in stop_words])
            text.append(line) #存原始字符串
    pickle.dump(text,open("./cache/text.bin","wb"))
    dictionary=corpora.Dictionary(sentences)
    dictionary.save("./cache/dict.bin")

    sentences_corpora=[]
    for sentence in sentences:
        sentences_corpora.append(dictionary.doc2bow(sentence))

    tfidf=models.TfidfModel(sentences_corpora)


    tfidf.save("./cache/tfidf.bin")

    #simlarity=similarities.Similarity('-Similarity-index',ifidf[sentences_corpora],num_features=len(dictionary))
    simlarity=similarities.MatrixSimilarity(tfidf[sentences_corpora],num_best=10,num_features=len(dictionary))
    simlarity.save("./cache/simlarity.bin")

sim=simlarity[tfidf[dictionary.doc2bow(list(jieba.cut(input_str)))]]
for index,rate in sim:
    print(text[index])




