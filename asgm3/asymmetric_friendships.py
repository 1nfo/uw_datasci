import sys
from MapReduce import *

fmr=MapReduce()

def reducer(person,friends):
    total=0
    for friend in list(set(friends)):
        total+=1
    fmr.emit((person,total))

def mapper(record):
    fmr.emit_intermediate(record[0],record[1])
    fmr.emit_intermediate(record[1],record[0])

if __name__=='__main__':
    fdata=open(sys.argv[1])
    fmr.execute(fdata,mapper,reducer)
