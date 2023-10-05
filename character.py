def edit_distance(str1 : str, str2 :str):
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    # 2次元配列を初期化
    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
    
    # 初期値を設定
    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j
    
    # 編集距離と操作回数を計算
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # 削除
                                   dp[i][j - 1],      # 挿入
                                   dp[i - 1][j - 1])  # 置換
    
    # 編集距離を返す
    edit_distance = dp[len_str1][len_str2]
    
    # 置換、挿入、削除の回数を返す
    num_replace = num_insert = num_delete = 0
    i, j = len_str1, len_str2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
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
    
    error_rate = (edit_distance / len_str1)
    
    return edit_distance, num_replace, num_insert, num_delete, error_rate
