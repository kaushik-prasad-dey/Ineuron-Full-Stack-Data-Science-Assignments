'''
  Question: 1
Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:
Integers in each row are sorted from right to left.
The first integer of each row is greater than the last integer of the previous row.
Example-: 

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: True
'''

def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage:
if __name__=="__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = binary_search_matrix(matrix,target = 3)
    print(result)