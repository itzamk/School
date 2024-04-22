'''
Andrew Kozempel
CMPSC 413
Lab 3
Fall 2023
'''

''' Video - focus more on second algo'''

# PART 1 NAIVE

def naive_search(text, pattern):

    # assign lengths of text and pattern
    m = len(pattern)
    n = len(text)
    
    # flag for match
    match = False

    # loops from start of text to (n-m)
    for i in range(n - m + 1):

        # if portion of text starting at index i
        # and length of m, return i
        if text[i:i + m] == pattern:
            print(f"Pattern found at index {i}")
            match = True

    # return -1 if no match
    if match == False:
        return -1

# Test Cases
print("\nNaive Test 1")
naive_search("This is a CMPSC 412 lab course. Students take this course along with CMPSC 462", "CMPSC")

print("\nNaive Test 2")
naive_search("This is a CMPSC 412 lab course. Students take this course along with CMPSC 462", "course")

print("\nNaive Test 3")
naive_search("AABAACAADAABAABAABBBBBAAABDCBA", "BBBBBA")

# PART 2 KMP

def kmp_search(text, pattern):

    # assign lengths of text and pattern
    m = len(pattern)
    n = len(text)
    
    # initialize lps array
    lps = [0] * m

    # length of the previous longest prefix suffix
    length = 0
    i = 1
    
    # calculate lps array
    while i < m:                                                    # EX. A B A B A C
                                                                    #     0 0 1 2 3 0
        # if chars match
        if pattern[i] == pattern[length]:

            # increment length, update lps, increment i
            length += 1
            lps[i] = length
            i += 1

        # if no match
        else:

            # if length not 0, update to previous length
            if length != 0:
                length = lps[length - 1]
            
            # lps[i] = 0, move to next char in pattern
            else:
                lps[i] = 0
                i += 1

    # pointers for text and pattern 
    i = 0
    j = 0 

    # flag to check if pattern is found at least once
    found = False
    
    # loop through the text
    while i < n:
                                                            # EX. 
                                                            # T:  A B A B C A B A B D
                                                            #
                                                            # P:            A B A B D
                                                            #               0 0 1 2 0
        # if chars match, increment i and j
        if pattern[j] == text[i]:
            i += 1
            j += 1

        # a match is found
        if j == m: 
            print("Pattern found at index", i - j)

            # reset pattern index, set flag to true
            j = lps[j - 1]
            found = True
            
        # chars dont match
        elif i < n and pattern[j] != text[i]:

            # mismatch after some matches
            if j != 0:
                # move j to next potential match
                j = lps[j - 1]

            # move up a char in text 
            else:
                i += 1

    # return -1 if no match
    if not found: 
        return -1

# Test Cases
print("\nKMP Test 1")
kmp_search("This is a CMPSC 412 lab course. Students take this course along with CMPSC 462", "CMPSC")

print("\nKMP Test 2")
kmp_search("This is a CMPSC 412 lab course. Students take this course along with CMPSC 462", "course")

print("\nKMP Test 3")
kmp_search("AABAACAADAABAABAABBBBBAAABDCBA", "BBBBBA")