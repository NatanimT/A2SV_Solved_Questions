class RandomizedSet:

    def __init__(self):
        self.values =[]
        self.hasmap = {}
    def insert(self, val: int) -> bool:
        if val in self.hasmap:
            return False  
        self.hasmap[val] = len(self.values)  

        self.values.append(val) 
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hasmap:
            return False
        index = self.hasmap[val]
        self.hasmap[self.values[-1]] = index
        del self.hasmap[val]
        self.values[index] = self.values[-1]
        self.values.pop()
        return True
    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()