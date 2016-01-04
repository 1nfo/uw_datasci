import sys
from MapReduce import *

joinmr=MapReduce()

def mapper(record):
    key=record[1]
    value=record
    joinmr.emit_intermediate(key,value)

def reducer(orderid,ord_list):
    order=[record[2:] for record in ord_list if record[0]=='order']
    item=[record[2:] for record in ord_list if record[0]=='line_item']
    for orec in order:
        for irec in item:
            joinmr.emit(tuple([orderid]+orec+irec))

if __name__=='__main__':
    jsdata=open(sys.argv[1])
    joinmr.execute(jsdata,mapper,reducer)
    count=0
    for i in joinmr.result:
        count+=1
        print 'record N0.',count,i
