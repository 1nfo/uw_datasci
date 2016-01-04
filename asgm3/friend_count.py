import sys
from MapReduce import *

fmr=MapReduce()

def reducer(person,count_list):
    fmr.emit((person,sum(count_list)))

def mapper(record):
    fmr.emit_intermediate(record[0],1)

if __name__=='__main__':
    fdata=open(sys.argv[1])
    fmr.execute(fdata,mapper,reducer)
