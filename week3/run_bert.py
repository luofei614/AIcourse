import  numpy as np
import pickle
import os
from bert_serving.client import BertClient
bc = BertClient(ip='localhost',check_version=False, check_length=False)
input_str=input("请输入一个问题：") or "越南旅游需要带插头转换器吗";
sentences=[]
sentences_token=[]
if os.path.isfile('./bert_token.pkl'):
    sentences,sentences_token=pickle.load(open('./bert_token.pkl','rb'))
else:
    with open('./questions.txt',encoding="utf-8") as f:
        for  line in f.readlines():
            sentences.append(line)
            sentences_token.append(bc.encode([line])[0])
    pickle.dump((sentences,sentences_token),open('./bert_token.pkl','wb'))
score = np.sum(bc.encode([input_str]) * sentences_token, axis=1) / np.linalg.norm(sentences_token, axis=1)
topk_idx = np.argsort(score)[::-1][:5]
for idx in topk_idx:
    print('> %s\t%s' % (score[idx], sentences[idx]))




