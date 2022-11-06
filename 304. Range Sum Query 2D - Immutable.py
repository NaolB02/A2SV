class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.preSum = []

        for i in range(len(matrix)):
            self.preSum.append([0] * len(matrix[i]))
        
        self.preSum[0][0] = matrix[0][0]

        for m in range(1, len(matrix)):
            self.preSum[m][0] = self.preSum[m - 1][0] + matrix[m][0]

        for j in range(len(matrix)):
            for k in range(1, len(matrix[j])):
                if j == 0:
                    self.preSum[j][k] = self.preSum[j][k - 1] + matrix[j][k]
                else:
                    self.preSum[j][k] = self.preSum[j - 1][k] + self.preSum[j][k - 1] - self.preSum[j - 1][k - 1] + matrix[j][k] 
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        Msum = 0
        if row1 == 0 and col1 == 0:
            Msum = self.preSum[row2][col2]
        
        elif row1 == 0:
            Msum = self.preSum[row2][col2] - self.preSum[row2][col1 - 1]
        
        elif col1 == 0:
            Msum = self.preSum[row2][col2] - self.preSum[row1 - 1][col2]
        
        else:
            Msum = self.preSum[row2][col2] - self.preSum[row1 - 1][col2] - self.preSum[row2][col1 - 1] + self.preSum[row1 - 1][col1 - 1]

        return Msum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
