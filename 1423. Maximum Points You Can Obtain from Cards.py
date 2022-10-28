class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start, end = 1, len(cardPoints) - k
        maxSum = sum(cardPoints[end:])
        temp = maxSum

        while end < len(cardPoints):
            temp = temp + cardPoints[start - 1] - cardPoints[end]
            maxSum = max(temp, maxSum)
            start += 1
            end += 1
        
        return maxSum
