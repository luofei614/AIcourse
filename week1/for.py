alist=["a","b","c","d"]
for item in alist:
    print(item)
for index,value in enumerate(alist):
    print(index,value)
print("遍历十次：")
for i in range(10):
    print(i)
print("倒着来：")
for i in range(9,-1,-1):
    print(i)
print("生成式")
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
