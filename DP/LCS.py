def longest_common_subsequence(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[len1][len2]
    lcs = [''] * lcs_length
    index = lcs_length - 1
    i, j = len1, len2

    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs[index] = seq1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    if isinstance(seq1, str) and isinstance(seq2, str):
        return ''.join(lcs)
    return lcs