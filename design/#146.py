# first try
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.dict = {}

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        else:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
            

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.queue.remove(key)
        elif len(self.dict) == self.capacity:
            lrkey = self.queue[0]
            self.queue.remove(lrkey)
            del self.dict[lrkey]           
        self.dict[key] = value
        self.queue.append(key)


# second try
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        else:
            self.dict.move_to_end(key)
            return self.dict[key]
            
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.move_to_end(key)
        elif len(self.dict) == self.capacity:
            self.dict.popitem(last=False)    
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)