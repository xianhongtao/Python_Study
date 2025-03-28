import numpy as np

def gaussian_elimination(aug_matrix, verbose=False):
    """使用NumPy实现高斯消元法化简增广矩阵
    verbose: 是否显示计算过程"""
    matrix = aug_matrix.copy().astype(float)
    if verbose:
        print("\n初始矩阵：")
        print(matrix)
    rows, cols = matrix.shape
    
    # 前向消元
    pivot_row = 0
    for col in range(cols-1):  # 最后一列是常数项不需要处理
        # 寻找主元
        pivot = np.argmax(np.abs(matrix[pivot_row:, col])) + pivot_row
        if matrix[pivot, col] == 0:
            continue  # 该列全零，跳过
            
        # 交换行
        matrix[[pivot_row, pivot]] = matrix[[pivot, pivot_row]]
        if verbose:
            print(f"\n交换行 {pivot_row+1} 和 {pivot+1} 后：")
            print(matrix)
        
        # 归一化主元行
        matrix[pivot_row] = matrix[pivot_row] / matrix[pivot_row, col]
        if verbose:
            print(f"\n主元行 {pivot_row+1} 归一化后：")
            print(matrix)
        
        # 消去下方元素
        for r in range(pivot_row+1, rows):
            matrix[r] = matrix[r] - matrix[r, col] * matrix[pivot_row]
            if verbose:
                print(f"\n消去行 {r+1} 元素后：")
                print(matrix)
            
        pivot_row += 1
        if pivot_row >= rows:
            break
            
    # 后向代入
    for col in reversed(range(cols-1)):
        for r in range(col):
            if matrix[r, col] != 0:
                factor = matrix[r, col]
                matrix[r] = matrix[r] - factor * matrix[col]
                if verbose:
                    print(f"\n后向代入处理行 {r+1} 后：")
                    print(matrix)
                
    # 保留两位小数并去除-0.0
    matrix = np.round(matrix, 2)
    matrix[np.abs(matrix) < 1e-10] = 0
    
    # 分析解的情况
    if verbose:
        rank_a = np.linalg.matrix_rank(matrix[:, :-1])
        rank_aug = np.linalg.matrix_rank(matrix)
        print(f"\n系数矩阵秩：{rank_a}，增广矩阵秩：{rank_aug}")
        if rank_a < rank_aug:
            print("=> 方程组无解")
        elif rank_a == matrix.shape[1]-1:
            print("=> 方程组有唯一解")
        else:
            print(f"=> 方程组有无穷解，自由变量数：{matrix.shape[1]-1 - rank_a}")
    
    return matrix

if __name__ == "__main__":
    # 示例增广矩阵
    test_matrix = np.array([
        [2, 1, -1, 8, 9],
        [-3, -1, 2, -11, 18],
        [-2, 1, 2, -3, 58],
        [4, 7, -6, 8, 63]
    ])
    
    result = gaussian_elimination(test_matrix, verbose=True)
    print("\n最终化简结果：")
    print(result)
