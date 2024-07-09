from typing import List


def reversePairs(self, a: List[int]) -> int:
        
        ''' 
        TC: O(n^2)
        cnt = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[i] > 2 * a[j]:
                    cnt += 1
        return cnt
        '''