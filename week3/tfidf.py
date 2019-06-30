from gensim import  corpora,similarities,models,matutils
import jieba
sentences=[]
stop_words = ["，", '。', '？', '.', ',', '.', '的', ' ', '\n']
with open('./questions.txt') as f:
    for line in f.readlines():
        sentences.append([word for word in jieba.cut(line) if word not in stop_words])
dictionary=corpora.Dictionary(sentences)
sentences_bow=[]
for s in sentences:
    sentences_bow.append(dictionary.doc2bow(s))



tfidf=models.TfidfModel(sentences_bow)


firstline=tfidf[sentences_bow[0]]
word_weights=sorted(firstline,key=lambda t:t[1],reverse=True)
print(word_weights)
