#https://leetcode.com/problems/decode-string/

def decode_string(s):
    decoded = ""
    i = 0
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            (n, j) = parse_num(s[i:])
            i += j
            (encoded, j) = scan_for_match(s[i:])
            decoded += n * decode_string(encoded)
            i += (j + 1)
        else:
            decoded += s[i]
            i += 1
    return decoded

def parse_num(s):
    for i, c in enumerate(s):
        if c >= '0' and c <= '9':
            continue
        else:
            return (int(s[:i]), i)               
            
def scan_for_match(s):
    bal = 0
    for i, c in enumerate(s):
        if s[i] == '[':
            bal -= 1
        elif s[i] == ']':
            bal += 1
        if bal == 0:
            return (s[1:i], i)
    return (None, -1)


        
