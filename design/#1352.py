class ProductOfNumbers:

    def __init__(self):
        self.pp = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pp = [1]
        else:
            self.pp.append(self.pp[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pp):
            return 0
        else:
            return self.pp[-1] // self.pp[-k-1]