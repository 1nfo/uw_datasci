import sys
from MapReduce2 import *

N=L=5

class MultiMR(MapReduce):
	def mapper(self,record):
		if record[0]=='a':
			for n in xrange(N):
				MapReduce.emit_intermediate(self,(record[1],n),(record[0],record[2],record[3]))
		if record[0]=='b':
			for l in xrange(L):
				MapReduce.emit_intermediate(self,(l,record[2]),(record[0],record[1],record[3]))

	def reducer(self,key,klist):
		mult=0
		for ii in klist:
			for jj in klist:
				if ii[0]=='a' and jj[0]=='b' and jj[1]==ii[1]:
					mult+=ii[2]*jj[2]
		MapReduce.emit(self,(key[0],key[1],mult))
if __name__=='__main__':
	mr=MultiMR()
	mr.execute(open(sys.argv[1]))