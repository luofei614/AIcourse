from gensim import  corpora,similarities,models,matutils
import jieba
sentences=[]
stop_words = ["，", '。', '？', '.', ',', '.', '的', ' ', '\n']
with open('./questions.txt') as f:
    for line in f.readlines():
        sentences.append([word for word in jieba.cut(line) if word not in stop_words])
dictionary=corpora.Dictionary(sentences)
#print(dictionary)
print(dictionary.token2id["西雅图"])
#bow1=dictionary.doc2bow([word for word in jieba.cut("西雅图的博物馆有哪些") if word not in stop_words])
#bow2=dictionary.doc2bow([word for word in jieba.cut("西雅图的博物馆有哪些") if word not in stop_words])
#sim=matutils.cossim(bow1,bow2)
#print(sim)
