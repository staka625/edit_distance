from typing import List
def word_edit_distance(test_list : List[str], ground_truth_list : List[str]):
    len_test_list = len(test_list)
    len_ground_truth_list = len(ground_truth_list)
    
    # 2次元配列を初期化
    dp = [[0 for _ in range(len_ground_truth_list + 1)] for _ in range(len_test_list + 1)]
    
    # 初期値を設定
    for i in range(len_test_list + 1):
        dp[i][0] = i
    for j in range(len_ground_truth_list + 1):
        dp[0][j] = j
    
    # 編集距離と操作回数を計算
    for i in range(1, len_test_list + 1):
        for j in range(1, len_ground_truth_list + 1):
            if test_list[i - 1] == ground_truth_list[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # 削除
                                   dp[i][j - 1],      # 挿入
                                   dp[i - 1][j - 1])  # 置換
    
    # 編集距離を返す
    edit_distance = dp[len_test_list][len_ground_truth_list]
    
    # 置換、挿入、削除の回数を返す
    num_replace = num_insert = num_delete = 0
    i, j = len_test_list, len_ground_truth_list
    while i > 0 or j > 0:
        if i > 0 and j > 0 and test_list[i - 1] == ground_truth_list[j - 1]:
            i -= 1
            j -= 1
        else:
            if i > 0 and (j == 0 or dp[i][j] == dp[i - 1][j] + 1):  # 削除
                num_delete += 1
                i -= 1
            elif j > 0 and (i == 0 or dp[i][j] == dp[i][j - 1] + 1):  # 挿入
                num_insert += 1
                j -= 1
            else:  # 置換
                num_replace += 1
                i -= 1
                j -= 1
    
    # 誤り率を計算
    edit_distance = dp[len_test_list][len_ground_truth_list]
    error_rate = (edit_distance / len_test_list)
    
    # 編集距離、削除、置換、挿入回数、誤り率を返す
    return edit_distance, num_replace, num_insert, num_delete, error_rate