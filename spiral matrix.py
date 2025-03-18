class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        r_first = 0
        r_last = 0
        c_first = m - 1
        c_last = n - 1
        while len(ans) < m * n:
            j = c_first
            while j <= c_last and len(ans) < m * n:
                ans.append(matrix[r_first][j])
                j += 1
            i = r_first + 1  
            while i <= r_last - 1 and len(ans) < m * n:
                ans.append(matrix[i][c_last])
                i += 1
            j = c_last
            while j >= c_first and len(ans) < m * n:
                ans.append(matrix[r_last][j])
                j -= 1
            i = r_last - 1
            while i >= r_first + 1 and len(ans) < m * n:
                ans.append(matrix[i][c_first])
                i -= 1
            r_first += 1
            c_first += 1
            r_last -= 1
            c_last -= 1
        return ans   
