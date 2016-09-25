#StringChains
'''
This seems liks a dynamic programming problem. The general approach is to walk
through the words in order of decreasing length, asking with each word x whether
or not x belongs to the longest chain. If it does, the result will be 1 + (the
answer to the subproblem of finding the longest chain of strings strictly shorter
then x. If it doesn't, the result will just be the longest chain or strings strictly
less than the previous upper bound, "last_taken" in the code below.
'''

def longestChain(words):
    if not words:
        return 0

    # sort words list so that longest strings come first
    words.sort(key=len)

    memo = [[0] * len(words) for _ in range(len(words))]
    
    return longest(words, memo)

def longest(words, memo):
    last_taken = None
    for i in len(words):
        if can_morph(last_taken, words[i]) else 0

    # consider the case where this subproblem has already been solved
    elif (i, last_taken) in memo:
        return memo[(i, last_taken)]

    # consider the case where we are free to either take word[i] into the solution,
    # or not to include it all 
    elif not last_taken or can_morph(last_taken, words[i]):
        memo[(i, last_taken)] = max(1 + longest(words, i+1, words[i], memo),
                                    longest(words, i+1, last_taken, memo))
        
    # finally, consider the case where we cannot accept word[i] into the currently
    # considered solution set
    else:
        memo[(i, last_taken)] = longest(words, i+1, last_taken, memo)
        
    return memo[(i, last_taken)]

# the question should always be: can we morph from_word (longer or as long as),
# into into_word?
def can_morph(from_word, into_word):
    if not from_word:
        return True
    if not (len(from_word) - len(into_word)) == 1:
        return False
    else:
        seen_diff = False
        i = 0
        while i < len(into_word):
            if from_word[i] != into_word[i]:
                if seen_diff:
                    return False
                else:
                    return from_word[i+1:] == into_word[i:]
            i += 1
        return True
                 
