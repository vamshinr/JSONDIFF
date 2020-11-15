class JsonCompare:

    def __init__(self,first_json,second_json):
        self.json1 = first_json
        self.json2 = second_json
        
    def ordered(self,ele):
        if isinstance(ele, dict):
            return sorted((key, self.ordered(value)) for key, value in ele.items())
        if isinstance(ele, list):
            return sorted(self.ordered(x) for x in ele)
        else:
            return ele
    
    def isEqual(self):
        return self.ordered(self.json1) == self.ordered(self.json2)
    
    def findDiff(self,flag=0):
        if len(self.json1) == len(self.json2):
            keys = []
            values = []
            for js1,js2 in zip(self.ordered(self.json1),self.ordered(self.json2)):
                if js1[0]!=js2[0]:
                    keys.append((js1[0],js2[0]))
                if js1[1]!=js2[1]:
                    values.append((js1[1],js2[1]))
        return keys,values
    
    def getDiffKeys(self):
        keys,values = self.findDiff()
        return keys
    
    def getDiffValues(self):
        keys,values = self.findDiff()
        return values
    
    def getDiff(self):
        keys,values = self.findDiff()
        return {"keys":keys, "values" :values}
