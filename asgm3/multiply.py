import sys
from MapReduce import *

#pre-define the sizes of a&b, which are L*M&M*N
N=4
L=4
matmr=MapReduce()

def mapper(record):
    if record[0]=='a':
        for n in range(N+1):
            matmr.emit_intermediate((record[1],n),(record[0],record[2],record[3]))
    if record[0]=='b':
        for l in range(L+1):
            matmr.emit_intermediate((l,record[2]),(record[0],record[1],record[3]))

def reducer(key,klist):
    d={}
    d['a']={}
    d['b']={}
    maxm=0
    for t in klist:
        maxm=max([maxm,t[1]])
        d[t[0]][t[1]]=t[2]
    mult=sum([d['a'].get(i,0)*d['b'].get(i,0) for i in range(maxm+1)])
    matmr.emit((key[0],key[1],mult))

if __name__=='__main__':
    matr=open(sys.argv[1])
    matmr.execute(matr,mapper,reducer)
