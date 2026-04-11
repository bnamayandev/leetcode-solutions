class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                arr = matrix[m]
                break
        else:
            return False

        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target > arr[m]:
                l = m + 1
            elif target < arr[m]:
                r = m - 1
            else:
                return True

        return False