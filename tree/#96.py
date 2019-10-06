class Solution(object):
    def numTrees(self, n):
        """
        The recursive equation.
        Let G(n) be the function which returns number of uninque BSTs.
		Consider [0,1,....i...., n]
        Let F(i,n) be the intermediate number of unique BSTs when i is the root.
        
        F(i,n) = G(i-1) * G(n-i) 
        When i is the root, there are i-1 nodes to left & n-i nodes to right
        
        for example -  to find G(4), we must also calculate G(3), G(2), G(1), G(0):
        G(4) ==> F(1,4) + F(2,4) + F(3,4) + F(4,4)
            for i = 1 --> F(1,4) = G(0) * G(3) = 1 * 5 = 5
            for i = 2 --> F(2,4) = G(1) * G(2) = 1 * 2 = 2
            for i = 3 --> F(3,4) = G(2) * G(1) = 2 * 1 = 2
            for i = 4 --> F(4,4) = G(3) * G(0) = 5 * 1 = 5
            Therefore G(4) = [G(0) * G(3)] + [G(1) * G(2)] + [G(2) * G(1)] + [G(3) * G(0)]
            G(4) = Σ(i = 1 to 4) G(i - 1) * G(4 - i)  
            G(4) = 5 + 2 + 2 + 5 = 14
        
        we know that G(0) = 1, G(1) = 1
        G(2) ==> F(1,2) + F(2,2)
            for i = 1 --> F(1,2) = G(0) * G(1) = 1
            for i = 2 --> F(2,2) = G(1) * G(0) = 1
            Therefore G(2) = 1 + 1 = 2
        
        G(3) ==> F(1,3) + F(2,3) + F(3,3)
            for i = 1 --> F(1,3) = G(0) * G(2) = 2 
            for i = 2 --> F(2,3) = G(1) * G(1) = 1
            for i = 3 --> F(3,3) = G(2) * G(0) = 2
            Therefore G(3) = 2 + 1 + 2 = 5
        

		To generalize:
                G(n) = Σ(i = 1 to n) G(i - 1) * G(n - i)  #Final formula
				
				
        Clearly we can see that previous values of G are recomputed again and again 
        hence we can memoize a.k.a Dynamic programming.
        """
        
        G = [0]*(n+1)
        G[0], G[1] = 1, 1
        
        #G(n) = Σ(i = 1 to n) G(i - 1) * G(n - i)
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        
        return G[n]