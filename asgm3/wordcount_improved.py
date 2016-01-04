from MapReduce2 import MapReduce
import sys

class wordcounter(MapReduce):
	def mapper(self,record):
		for w in record[1].split():
			MapReduce.emit_intermediate(self,w,1)

	def reducer(self,key,list_of_v):
		t=0
		for v in  list_of_v:
			t+=v
		MapReduce.emit(self,(key,t))

if __name__=="__main__":
	wc=wordcounter();
	wc.execute(open(sys.argv[1]))