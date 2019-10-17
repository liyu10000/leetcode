class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        num_already = sum([c for c, g in zip(customers, grumpy) if g == 0])
        num_toadd = sum([customers[i] for i in range(X) if grumpy[i] == 1])
        num_toadd2 = num_toadd
        for i in range(len(customers) - X):
            if grumpy[i]:
                num_toadd -= customers[i]
            if grumpy[i+X]:
                num_toadd += customers[i+X]
            num_toadd2 = max(num_toadd2, num_toadd)
        return num_already + num_toadd2