import collections

def palsub(s):
    occs = collections.defaultdict(list)
    max_len = 1
    max_sub_i = 0
    max_sub_j = 1
    for i, c in enumerate(s):
        if len(occs[c]) > 0:
            for j in occs[c]:
                if (i + 1 - j) > max_len and is_pal(s[j:i+1]):
                    max_len = i + 1 - j
                    max_sub_i = i
                    max_sub_j = j
                    break
                    
        occs[c].append(i)
    return s[max_sub_j:max_sub_i + 1]

def is_pal(s):
    l = len(s)
    if l % 2 == 0:
        return s[:l//2] == (s[l//2:])[::-1]
    else:
        return s[:l//2] == (s[l//2+1:])[::-1]
