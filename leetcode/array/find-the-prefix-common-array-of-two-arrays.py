# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        seenA = set() # 1, 3
        seenB = set() # 3, 1
        counter = 0 # 2

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            if A[i] == B[i]:
                counter += 1
                result.append(counter)
                continue

            if A[i] in seenB:
                counter += 1
            
            if B[i] in seenA:
                counter += 1


            result.append(counter)

        return result
