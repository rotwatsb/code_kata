
def isSubsequence(s, t):
    for c in t:
        if c == s[0]:
            if len(s) > 1:
                s = s[1:]
            else:
                return True
    return False
