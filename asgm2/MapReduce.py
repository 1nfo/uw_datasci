import json,sys

class MapReduce:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        sys.stdout.write('mapping\n')
        count=0
        for record in data:
            count+=1
            mapper(record)
            sys.stdout.write(str(count)+'/'+str(len(data))+'\r')
            sys.stdout.flush()

        count=0
        for key in self.intermediate:
            count+=1
            sys.stdout,write('reducing\n')
            reducer(key, self.intermediate[key])
            sys.stdout.write(str(count)+'/'+str(len(self.intermediate))+'\r')
            sys.stdout.flush()

        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()
        for item in self.result:
            print jenc.encode(item)
