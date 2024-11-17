# Status: needs revisit
def kmp_search(pattern, text):
    def compute_lps(pat):
        lps = [0] * len(pat)
        length = 0
        for i in range(1, len(pat)):
            while length > 0 and pat[i] != pat[length]:
                length = lps[length - 1]
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
        return lps

    lps = compute_lps(pattern)
    matches = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                matches.append(i - j + 1)
                j = lps[j - 1]
    return matches