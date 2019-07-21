import GstoreConnector
IP = "127.0.0.1"
Port = 9000
username = "root"
password = "123456"
sparql='''select ?s ?p ?o   where
{
  ?s ?p ?o.
}
limit 10
'''
"""

sparql='''select ?name   where
{
  ?id <name:cn> ?name.
  ?id <type:credits> "喜剧之王".
}
'''

#星爷和吴孟达共同演出的影片
sparql='''select ?movie_name   where
{
  ?id <name:cn> "周星驰".
  ?id2 <name:cn> "吴孟达".
  ?id <type:credits> ?movie_name.
  ?id2 <type:credits> ?movie_name.
}
'''


#统计计数
sparql='''select (count(?movie_name) as ?c)   where
{
  ?id <name:cn> "周星驰".
  ?id2 <name:cn> "吴孟达".
  ?id <type:credits> ?movie_name.
  ?id2 <type:credits> ?movie_name.
}
'''
#name="周星驰"
name="Stephen Chow"
sparql='''select ?movie_name   where
{
   {?id <name:en> "%s".} UNION  {?id <name:cn> "%s".}.
   ?id <type:credits> ?movie_name.
}
''' % (name,name)

#正则
sparql='''select * where {
  ?id <name:en> ?name.
  FILTER regex(?name,'Stephen','i')
}
'''


#对比大小
sparql='''
select ?name ?count  where {
  ?id <type:vote_count> ?count.
  ?id <name:cn> ?name.
  filter (?count>"100"^^<http://www.w3.org/2001/XMLSchema#integer>)
}
'''

#order by
sparql='''
select * where {
  ?id <type:vote_count> ?count.
}
ORDER BY DESC(?count)
LIMIT 10
'''

"""

print(sparql)

gc =  GstoreConnector.GstoreConnector(IP, Port, username, password)
#res = gc.drop("movie",False)
#res = gc.build("movie","data/movies.nt")
#print(res)
res = gc.load("movie")
res = gc.query("movie", "json", sparql)
print("query result####")
print(res)
