print("列表")
alist=["a","b","c"]
alist.append("d")
print(alist)
print(alist+["e","f"])
print(alist.pop())
print(alist)
print(alist.pop(0))
print(alist)
alist.insert(0,"aa")
alist.insert(2,"222")
print(alist)
print(alist[-1])
print(alist[1:-1])
del alist[0] 
print(alist)


print("元祖")
atuple=("a","b","c")
#atuple.append("d")
#del atuple[0]
a,b,c=atuple
print(a)
onetuple=("a",)
print(onetuple)

print("集合")
aset={"a","b","c"}
aset.add("a")
print(aset)
print(aset & {"a","b","f"})
print(aset | {"a","b","f"})
print("词典")
adict={"a":"aaa","b":"bbb","c":"ccc"}
print(adict["a"])
print(adict.get("f","default"))
adict.update({"b":"b2b2","f":"ffff"})
print(adict)
adict.pop("a")
print(adict)
print(adict.keys())
print(adict.values())

print('类型转换')

theList=["a","b","c"]
theTuple=tuple(theList)
print(theTuple)
print(list(theTuple))
print(set(theList))
print(dict(zip(["a","b","c"],["aaaa","bbb","ccc"])))

print("a" in ["a","b","c"])
print("a" in {"a":"aaa","b":"bbb","c":"ccc"})
print(len({"a":"aaa","b":"bbb","c":"ccc"}))

