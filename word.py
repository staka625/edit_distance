from typing import List
def word_edit_distance_by_str(test_str_split_by_char:str,ground_truth_by_char:str,split_char = " "):
    print(test_str_split_by_char.split())
    return word_edit_distance(test_str_split_by_char.split(),ground_truth_by_char.split())

def word_edit_distance(test_list : List[str], ground_truth_list : List[str]):
    elements_to_remove = [".",",","。","、"," ",",","\n"]
    test_list = [x for x in test_list if x not in elements_to_remove]
    len_test_list = len(test_list)
    len_ground_truth_list = len(ground_truth_list)
    
    dp = [[0 for _ in range(len_ground_truth_list + 1)] for _ in range(len_test_list + 1)]
    
    for i in range(len_test_list + 1):
        dp[i][0] = i
    for j in range(len_ground_truth_list + 1):
        dp[0][j] = j
    
    for i in range(1, len_test_list + 1):
        for j in range(1, len_ground_truth_list + 1):
            if test_list[i - 1] == ground_truth_list[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # 削除
                                   dp[i][j - 1],      # 挿入
                                   dp[i - 1][j - 1])  # 置換
    
    edit_distance = dp[len_test_list][len_ground_truth_list]
    
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
    
    edit_distance = dp[len_test_list][len_ground_truth_list]
    error_rate = (edit_distance / len_test_list)
    
    return edit_distance, num_replace, num_insert, num_delete, error_rate