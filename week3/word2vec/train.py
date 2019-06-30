from gensim import corpora,models,similarities
import os
import json
import re
import jieba
from helper import model2pca,tensorflow_visualize

sentences=[]
with open('./story.json','r',encoding="utf-8") as f:
    for line in f.readlines():
        json_data = json.loads(line)
        content = json_data['content']
        raw_sentences = re.split(r'[。，]|\n|<br>|\xa0\xa0\xa0\xa0', content)
        for s in raw_sentences:
            if s.strip() != '':
                sentences.append(list(jieba.cut(s)))



model=models.Word2Vec(sentences,50,sg=0)
model.save('./output/story.model.bin')
model2pca(model,'./output/pca.png',1000)
tensorflow_visualize(model,'./output',50)
