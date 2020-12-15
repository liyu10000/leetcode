import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        flag = not val in self.s
        if flag:
            self.s.add(val)
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        flag = val in self.s
        if flag:
            self.s.remove(val)
        return flag
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.s, 1)[0]