def name(a,b,c,d):
    return a+b+c+d
print(name("aaa","bbb",d="ddd",c="ccc"))

#词权重排序
cities=[
    ('上海',9),
    ('重庆',3),
    ('武汉',2),
    ('郑州',1),
    ('广州',8),
    ('北京',10),
    ('深圳',7),
    ('成都',6),
    ('重庆',5),
    ('天津',4)
]

sorted_cities=sorted(cities,key=lambda city:city[1],reverse=True)
print(sorted_cities)

