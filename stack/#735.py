# stack, with recursive call, inefficient
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n < 2:
            return asteroids
        flag = False
        s = []
        for a in asteroids:
            if s and s[-1] > 0 > a:
                if s[-1] == -a:
                    s.pop()
                elif s[-1] < -a:
                    s[-1] = a
                flag = True
            else:
                s.append(a)
        return self.asteroidCollision(s) if flag else s

# stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n < 2:
            return asteroids
        s = []
        for i in range(n):
            s.append(asteroids[i])
            while len(s) > 1 and s[-2] > 0 > s[-1]:
                if s[-2] == -s[-1]:
                    s.pop()
                elif s[-2] < -s[-1]:
                    s[-2] = s[-1]
                s.pop()
        return s