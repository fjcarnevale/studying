import sorting

def expect_equal(a, b, name):
    if a == b:
        print("Pass: " + name)
    else:
        print("Fail: " + name)

# Question 1.1a
def unique_characters(S):
    chars = {}

    for c in S:
        if c in chars:
            return False
        chars[c] = True

    return True

# Test 1.1a
S = "abcdefg"
expect_equal(unique_characters(S), True, "1.1a Unique")
S = "abcdeefg"
expect_equal(unique_characters(S), False, "1.1a Not Unique")


# Question 1.1b
def unique_characters_no_hash(S):
        
    A = list(S)

    sorting.quicksort(A)

    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return False

    return True

# Test 1.1b
S = "abcdefg"
expect_equal(unique_characters_no_hash(S), True, "1.1b Unique")
S = "aebcdefg"
expect_equal(unique_characters_no_hash(S), False, "1.1b Not Unique")

# Question 1.2

def reverse_string(S):
    A = list(S)
    i = 0
    j = len(A) - 1

    while i < j:
        A[i],A[j] = A[j],A[i]
        i += 1
        j -= 1

    return "".join(A)


# Test 1.2
S = "abcde"
expect_equal(reverse_string(S), "edcba", "1.2 Odd")
S = "abcdef"
expect_equal(reverse_string(S), "fedcba", "1.2 Even")


# Question 1.3
def is_permutation(A,B):
    A = list(A)
    B = list(B)

    if len(A) != len(B):
        return False

    letters = {}
    for c in A:
        if c not in letters:
            letters[c] = {"A":0, "B":0}
        letters[c]["A"] += 1

    for c in B:
        if c not in letters:
            return False
        letters[c]["B"] += 1

    for c in letters:
        if letters[c]["A"] != letters[c]["B"]:
            return False

    return True

# Test 1.3
A = "abcde"
B = "aebdc"
expect_equal(is_permutation(A,B), True, "1.3 Match")
B = "aebdcf"
expect_equal(is_permutation(A,B), False, "1.3 Mismatch Different Length")
B = "abdcz"
expect_equal(is_permutation(A,B), False, "1.3 Mismatch Different Letters")















