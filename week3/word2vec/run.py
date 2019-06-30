from gensim import corpora,models,similarities

model=models.Word2Vec.load('./output/story.model.bin')

print(model["陈军"])
quit();


input_str=input("请输入：")

arr=input_str.split(" ")
if len(arr)>1 :
    print(arr)
    rate=model.similarity(arr[0],arr[1])
    print("相似度：%s" % rate)
else:
    topn=model.most_similar([arr[0]])
    print(topn)

