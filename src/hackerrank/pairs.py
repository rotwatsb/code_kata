#https://www.hackerrank.com/challenges/pairs
def pairs(a,k):
    # a is the list of numbers and k is the difference value

    a.sort()
    i = j = 0
    answer = 0
    while j < len(a):
        if i != j:
            dif = a[j] - a[i]
            if dif == k:
                answer += 1
                j += 1
            elif dif > k:
                i += 1
            else:
                j += 1
        else:
            j += 1
    return answer

