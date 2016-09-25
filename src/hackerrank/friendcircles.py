#Friend Circles
'''
This seems like a variation of a union-find type problem. The strategy here 
is to keep a hierarchical array of pointers where array[i] = j indicates 
that friend i is friends with friend j. Then with each new friend pair,
join the friend circles by changing the 'head' of the smaller friend
circle to that of the larger. Keep track of friend circles sizes for
efficiency. The runtime should be upperbounded at O(n^2 * log n) time,
where n is len(friends). The main double loop does n^2 / 2 iterations, but 
each iteration makes two calls to find_head, which take log n time. Counting
the final number of distinct friend circles is just O(n) time.
'''

def friendCircles(friends):
    # each friend is initially only friends with him/herself
    friend_array = [x for x in range(len(friends))]
    
    # and keep track of circles sizes
    circle_sizes = [1 for _ in range(len(friends))]
    for i in range(len(friends)):
        for j in range(i, len(friends)):
            if i != j and friends[i][j] == 'Y':
                i_head = find_head(i, friend_array)
                j_head = find_head(j, friend_array)
                
                if circle_sizes[i_head] >= circle_sizes[j_head]:
                    circle_sizes[i_head] += circle_sizes[j_head]
                    friend_array[j_head] = i_head
                else:
                    circle_sizes[j_head] += circle_sizes[i_head]
                    friend_array[i_head] = j_head

    # now sum up unique circles. all members of a unqie friend circle now
    # point back to the same head, so we can just count the unique heads,
    # i.e., friend_array[i] == i 
    count = 0
    for i in range(len(friend_array)):
        if friend_array[i] == i:
            count += 1

    return count

def find_head(i, friend_array):
    if friend_array[i] == i:
        return i
    else:
        return find_head(friend_array[i], friend_array)
                
test0 = ["Y"]
            
test1 = ["YNNN",
         "NYNN",
         "NNYN",
         "NNNY"]

test2 = ["YYNN",
         "YYNN",
         "NNYN",
         "NNNY"]

test3 = ["YYNN",
         "YYYN",
         "NYYY",
         "NNYY"]


