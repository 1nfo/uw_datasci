import sys
from MapReduce import *

indexmr=MapReduce()
def mapper(record):
    book=record[0]
    words=record[1].split()
    for word in words:
        indexmr.emit_intermediate(word,book)

def reducer(word,books):
    indexmr.emit((word,books))

if __name__=='__main__':
    data=open(sys.argv[1])
    indexmr.execute(data,mapper,reducer)
