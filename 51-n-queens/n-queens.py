class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []

        def issafe(mat, r, c):

            
            for i in range(r, -1, -1):
                if mat[i][c] == "Q":
                    return False

             
            r1 = r
            c1 = c

            while c1 < len(mat[0]) and r1 > -1:
                if mat[r1][c1] == "Q":
                    return False

                c1 += 1
                r1 -= 1

             
            r1 = r
            c1 = c

            while c1 > -1 and r1 > -1:
                if mat[r1][c1] == "Q":
                    return False

                c1 -= 1
                r1 -= 1

            return True

        board = [["."] * n for i in range(n)]

        def fun(mat, r, n):

            if r == n:
                l = []

                for i in mat:
                    l.append("".join(i))

                ans.append(l.copy())
                return

            for c in range(n):

                if issafe(mat, r, c):

                    mat[r][c] = "Q"

                    fun(mat, r + 1, n)

                    mat[r][c] = "."

        fun(board, 0, n)

        return ans