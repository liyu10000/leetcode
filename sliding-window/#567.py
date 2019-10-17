class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        for c in s1:
            count1[ord(c) - ord('a')] += 1
        
        for i in range(l2):
            if i - l1 >= 0:
                count2[ord(s2[i-l1]) - ord('a')] -= 1
            count2[ord(s2[i]) - ord('a')] += 1
            if count2 == count1:
                return True
        return False