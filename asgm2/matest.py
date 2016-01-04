import sqlite3,sys
from MapReduce import *

conn=sqlite3.connect('reuters.db')
print 'connection has been created successfully\n'

query='select * from frequency'
conn.execute(query)
cursor=conn.execute(query)
print 'selected successfully\n'

matrix=[]
docid=set()
term=set()
for record in cursor:
    matrix.append(record)
    docid.add(record[0].encode('utf-8'))
    term.add(record[1].encode('utf-8'))
docid=list(docid)
term=list(term)
conn.close()

#pre-define the sizes of a&b, which are L*M&M*N
M=len(docid)
matmr=MapReduce()

def mapper(record):
    for m in range(M+1):
        matmr.emit_intermediate((record[0],m),('a',record[1],record[2]))
        matmr.emit_intermediate((m,record[0]),('b',record[1],record[2]))

def reducer(key,klist):
    d={}
    d['a']={}
    d['b']={}
    maxm=0
    for t in klist:
        d[t[0]][t[1]]=t[2]
    mult=sum([d['a'].get(i,0)*d['b'].get(i,0) for i in term])
    matmr.emit((key[0],key[1],mult))

if __name__=='__main__':
    matmr.execute(matrix,mapper,reducer)

