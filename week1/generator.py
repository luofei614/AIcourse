def gen():
    for i in range(5):
        yield i
    return 'done'


def gensend():
    for i in range(5):
        y=yield i
        print("y is :%s" % y)

g=gen()
print(g)
print(next(g))
print('for循环')
for i in g:
    print(i)
print('异常')
try:
    g2=gen();
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))
except StopIteration as ret:
    print('result:')
    print(ret.value)

print('send传值')

gsend=gensend()
gsend.send(None)
gsend.send('value')


