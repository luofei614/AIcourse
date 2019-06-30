import jieba
seg_list=jieba.cut("明天台南县的天气")
print(list(seg_list))
jieba.add_word('张三')
seg_list2=jieba.cut("张三说的确实在理")
print(list(seg_list2))