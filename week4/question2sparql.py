
import re
import json
import GstoreConnector
IP = "127.0.0.1"
Port = 9000
username = "root"
password = "123456"
gc =  GstoreConnector.GstoreConnector(IP, Port, username, password)
gc.load("movie")
class Rule():
    def __init__(self, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        m=re.match(self.condition,sentence)
        if m:
            self.action(*m.groups())
            return True


def getMovie(p1):
    sparql='''select ?movie_name   where
    {
    ?id <name:cn> "%s".
    ?id <type:credits> ?movie_name.
    }
    ''' % p1
    ret_str=gc.query("movie", "json", sparql)
    ret=json.loads(ret_str)
    for item in ret['results']['bindings']:
        print(item['movie_name']['value'])

def sameMovie(p1,p2):
    sparql='''select ?movie_name   where
    {
    ?id <name:cn> "%s".
    ?id2 <name:cn> "%s".
    ?id <type:credits> ?movie_name.
    ?id2 <type:credits> ?movie_name.
    }
    ''' % (p1,p2)
    ret_str=gc.query("movie", "json", sparql)
    ret=json.loads(ret_str)
    for item in ret['results']['bindings']:
        print(item['movie_name']['value'])

def getActors(movie_name):
    sparql='''select ?actor_name   where
    {
    ?id <name:cn> ?actor_name.
    ?id <type:credits> "%s".
    }
    ''' % (movie_name)
    ret_str=gc.query("movie", "json", sparql)
    ret=json.loads(ret_str)
    for item in ret['results']['bindings']:
        print(item['actor_name']['value'])


rules=[
    Rule(r'(.*?)演了什么电影',getMovie),
    Rule(r'(.*?)和(.*?)共同演的电影',sameMovie),
    Rule(r'(.*?)的演员',getActors)
]

question=input("请输入问题：")
for r in rules:
    answer=r.apply(question)
    if answer:
        break
