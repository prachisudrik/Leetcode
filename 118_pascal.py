class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [0] * (i+1)
            row[0],row[-1] = 1, 1
            for col in range(1, len(row)-1):
                row[col] = triangle[i-1][col-1]+triangle[i-1][col]
            triangle.append(row)
        return triangle
        