import sys
from MapReduce import *

dnarm=MapReduce()

def mapper(record):
    kind=record[0]
    trimseq=record[1][0:-10]
    dnarm.emit_intermediate(trimseq,kind)

def reducer(trimseq,kinds):
    dnarm.emit((trimseq,kinds))

if __name__=='__main__':
    DNAseq=open(sys.argv[1])
    dnarm.execute(DNAseq,mapper,reducer)
    print [i[1] for i in dnarm.result]
