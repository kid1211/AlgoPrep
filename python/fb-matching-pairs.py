# Matching Pairs
# Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
# A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
# Note: This means you must swap two characters at different indices.
# Signature
# int matchingPairs(String s, String t)
# Input
# s and t are strings of length N
# N is between 2 and 1,000,000
# Output
# Return an integer denoting the maximum number of matching pairs
# Example 1
# s = "abcd"
# t = "adcb"
# output = 4
# Explanation:
# Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
# Therefore, the number of matching pairs of s and t will be 4.
# Example 2
# s = "mno"
# t = "mno"
# output = 1
# Explanation:
# Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.
import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here
    s_looking_for_match = {}
    unmatched_idx = []

    for i in range(len(s)):
        if s[i] != t[i]:
            s_looking_for_match[s[i]] = s_looking_for_match.get(s[i], []) + [i]
            unmatched_idx += [i]

    if len(unmatched_idx) < 2:
        return len(s) - len(unmatched_idx) - (2 - len(s_looking_for_match))

    maxInc = 0
    for idx in unmatched_idx:
        # idx => 1
        # t[idx] = d
        # s[idx] = b

        # check if d in s_looking_for_match, if so return => 3
        # check t[3] = s[idx]
        if t[idx] not in s_looking_for_match:
            continue

        for idx_in_s_matches_t_idx in s_looking_for_match[t[idx]]:
            if t[idx_in_s_matches_t_idx] == s[idx]:
                maxInc = max(2, maxInc)
            else:
                maxInc = max(1, maxInc)

    return len(s) - len(unmatched_idx) + maxInc

    # if they are all the same -2
    # if they have only 1 that is not the same -1
    # if there are two that is not the same and these two are the same + 2
    # if there are two that is not the same and there are


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.


def printInteger(n):
    print("[", n, "]", sep="", end="")


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = "\u2713"
    wrongTick = "\u2717"
    if result:
        print(rightTick, "Test #", test_case_number, sep="")
    else:
        print(wrongTick, "Test #", test_case_number, ": Expected ", sep="", end="")
        printInteger(expected)
        print(" Your output: ", end="")
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

