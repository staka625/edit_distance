def edit_distance(str1 : str, str2 :str,is_remove=True):
    if(is_remove):
        str1 = str1.replace(".","").replace(",","").replace("。","").replace("、","").replace(" ","").replace("\n","")
        str2 = str2.replace(".","").replace(",","").replace("。","").replace("、","").replace(" ","").replace("\n","")

    len_str1 = len(str1)
    len_str2 = len(str2)
    
    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
    
    for i in range(len_str1 + 1):
        dp[i][0] = i
    for j in range(len_str2 + 1):
        dp[0][j] = j
    
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # 削除
                                   dp[i][j - 1],      # 挿入
                                   dp[i - 1][j - 1])  # 置換
    
    edit_distance = dp[len_str1][len_str2]
    
    num_replace = num_insert = num_delete = 0
    i, j = len_str1, len_str2
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1
        else:
            if i > 0 and (j == 0 or dp[i][j] == dp[i - 1][j] + 1): 
                num_delete += 1
                i -= 1
            elif j > 0 and (i == 0 or dp[i][j] == dp[i][j - 1] + 1): 
                num_insert += 1
                j -= 1
            else:  
                num_replace += 1
                i -= 1
                j -= 1
    
    error_rate = (edit_distance / len_str1)
    
    return edit_distance, num_replace, num_insert, num_delete, error_rate
